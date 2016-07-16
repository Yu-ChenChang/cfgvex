import CFG_pb2
import os, sys
import struct
def error_exit(msg):
	print >> sys.stderr, msg
	exit()

## enum of IR type ##
class IRTYPE:
	GET, PUT, Xor, Add, Sub, BitOper, LD, ST, Ass = range(9)

def __findIRtype(leftside,rightside):
## leftside operator ##
	if "PUT" in leftside:
		target = leftside.partition('(')[-1].rpartition(')')[0]
		varName = rightside.strip()
		print target
		return (varName,[target,IRTYPE.PUT])

	elif "ST" in leftside:
		if "STle" in leftside:
			target = leftside.partition('(')[-1].rpartition(')')[0]
			varName = rightside.strip()
			print target
			return (varName,[target,IRTYPE.ST])

## rightside operator ##
	if "GET" in rightside:
		if "I32" in rightside or "I64" in rightside:
			target = rightside.partition('(')[-1].rpartition(')')[0]
			varName = leftside.strip()
			print target
			return (varName,[target,IRTYPE.GET])

	elif "Xor" in rightside:
		if "Xor32" in rightside or "Xor64" in rightside:
			target = rightside.partition('(')[-1].rpartition(',')[0]
			target2 = rightside.partition(',')[-1].rpartition(')')[0]
			varName = leftside.strip()
			print target
			return (varName,[target,IRTYPE.Xor,target2])
	
	
	elif "Add" in rightside:
		if "Add32" in rightside or "Add64" in rightside:
			target = rightside.partition('(')[-1].rpartition(',')[0]
			target2 = rightside.partition(',')[-1].rpartition(')')[0]
			varName = leftside.strip()
			print target
			return (varName,[target,IRTYPE.Add,target2])

	elif "Sub" in rightside:
		if "Sub32" in rightside or "Sub64" in rightside:
			target = rightside.partition('(')[-1].rpartition(',')[0]
			target2 = rightside.partition(',')[-1].rpartition(')')[0]
			varName = leftside.strip()
			print target
			return (varName,[target,IRTYPE.Sub,target2])

	elif "Shl" in rightside or "And" in rightside or "Mul" in rightside:
		#if "Shl32" in rightside or "Shl64" in rightside:
		target = rightside.partition('(')[-1].rpartition(',')[0]
		target2 = rightside.partition(',')[-1].rpartition(')')[0][2:]
		if '0x' in target2:
			if len(target2) <=10:
				target2 = struct.unpack('>i', rightside.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
			else:
				target2 = struct.unpack('>q', rightside.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
		varName = leftside.strip()
		print target
		return (varName,[target,IRTYPE.BitOper,target2])

	elif "LD" in rightside:
		if "LDle" in rightside:
			target = rightside.partition('(')[-1].rpartition(')')[0]
			varName = leftside.strip()
			print target
			return (varName,[target,IRTYPE.LD])

	## simulated as Ass ##
	elif any(irInst in rightside for irInst in ("F32toF64",'64to32','32Uto64','64to1')):
		target = rightside.partition('(')[-1].rpartition(')')[0]
		varName = leftside.strip()
		print target
		print target
		return (varName,[target,IRTYPE.Ass])

	## simulated as Ass ##
	elif any(irInst in rightside for irInst in ('x86g_calculate_condition', 'amd64g_calculate_condition','x86g_calculate_eflags_c')):
		target = rightside.partition('(')[-1].rpartition(')')[0].split(',')[1]
		varName = leftside.strip()
		print target
		print target
		return (varName,[target,IRTYPE.Ass])

	elif ('t' in rightside or '0x' in rightside) and 't' in leftside:
		target = rightside.strip()
		varName = leftside.strip()
		print target
		return (varName,[target,IRTYPE.Ass])



def tvarToExp(tvar, varName):
	if tvar[varName][1] > 0:
		memory = tvar[varName][0] + '_add_' + hex(tvar[varName][1])
	elif tvar[varName][1] == 0:
		memory = tvar[varName][0]
	else:
		memory = tvar[varName][0] + '_sub_' + hex(abs(tvar[varName][1]))
	return memory

## return uninitialized register or memory location that has been read ##
def analysisIR(inst_ir,initList):
	uniList = []
	tvar = {}
	filtered = ['AbiHint','if','32to1']

	print inst_ir.split('\n')[0]
	for line in inst_ir.split('\n'):
		print "-----ir start-----"
		print line
		filflag = False
		if any(irst in line for irst in filtered):
			continue
		try:
			ind = line.index('=')
		except:
			continue
		leftside = line[:ind].strip()
		rightside = line[ind+1:].strip()
		try:
			varName,IRinfo = __findIRtype(leftside,rightside)
		except:
			error_exit("Err: Found undefined IR Type in \"%s\"" %line)
		print IRinfo[1]
		## combine each IR inst result ##
		if IRinfo[1] == IRTYPE.GET:
			tvar[varName] = (IRinfo[0],0,False)

		elif IRinfo[1] in (IRTYPE.Xor ,IRTYPE.Add ,IRTYPE.Sub):
			if '0x' in IRinfo[2]:
				if len(IRinfo[2]) <=10:
					tvar[varName] = (tvar[IRinfo[0]][0] , tvar[IRinfo[0]][1] + struct.unpack('>i', IRinfo[2][2:].decode('hex'))[0],False)
				else:
					tvar[varName] = (tvar[IRinfo[0]][0] , tvar[IRinfo[0]][1] + struct.unpack('>q', IRinfo[2][2:].decode('hex'))[0],False)
			else:
				tvar[varName] = (tvar[IRinfo[0]][0] , tvar[IRinfo[0]][1] + tvar[IRinfo[2]][1],False)

		## simulated as Ass ##
		elif IRinfo[1] == IRTYPE.BitOper:
			tvar[varName] = tvar[IRinfo[0]]

		elif IRinfo[1] == IRTYPE.LD:
			tvar[varName] = (tvar[IRinfo[0]][0] , tvar[IRinfo[0]][1], True) ## True means this is not address but content is loaded ##

		elif IRinfo[1] == IRTYPE.Ass:
			if '0x' in IRinfo[0]:
				if len(IRinfo[0]) <=10:
					tvar[varName] = ('memory' , struct.unpack('>i', IRinfo[0][2:].decode('hex'))[0],False)
				else:
					tvar[varName] = ('memory' , struct.unpack('>q', IRinfo[0][2:].decode('hex'))[0],False)
			else:
				tvar[varName] = tvar[IRinfo[0]]

## leftside operator ##
		elif IRinfo[1] == IRTYPE.PUT:
			if '0x' not in varName:
				if tvar[varName][0] != 'memory':
					memory = tvarToExp(tvar, varName)

					## If the register is not updating itself (like esp = esp-4) ##
					if tvar[varName][2] == True and memory not in initList and tvar[varName][0] != IRinfo[0]:
						if memory not in uniList:
							print "uniList add: " + str(memory)
							uniList += [memory]
			if IRinfo[0] not in initList:
				print "initList add: " + str(IRinfo[0])
				initList += [IRinfo[0]]

		elif IRinfo[1] == IRTYPE.ST:
			#leftside
			if '0x' not in varName:
				memory = tvarToExp(tvar, varName)
				print memory
				if memory not in initList and memory not in uniList:
					print "uniList add: " + str(memory)
					uniList += [memory]

			#rightside
			memory = tvarToExp(tvar, IRinfo[0])
			if memory not in initList:
				print "initList add: " + str(memory)
				initList += [memory]
		print "uniList: "
		print uniList	
		print "initList: "
		print initList
	return uniList
	

	
