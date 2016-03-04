import CFG_pb2
import os, sys
import struct
def error_exit(msg):
	print >> sys.stderr, msg
	exit()

## enum of IR type ##
class IRTYPE:
	GET, PUT, Add, Sub, Shl, LD, ST, Ass = range(8)

def __findIRtype(leftside,rightside):
## rightside operator ##
	if "GET" in rightside:
		if "I32" in rightside or "I64" in rightside:
			target = rightside.partition('(')[-1].rpartition(')')[0]
			var = leftside.strip()
			#print target
			return (var,[target,IRTYPE.GET])
	
	
	elif "Add" in rightside:
		if "Add32" in rightside or "Add64" in rightside:
			target = rightside.partition('(')[-1].rpartition(',')[0]
			target2 = rightside.partition(',')[-1].rpartition(')')[0][2:]
			if '0x' in target2:
				target2 = struct.unpack('>i', rightside.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
			var = leftside.strip()
			#print target
			return (var,[target,IRTYPE.Add,target2])

	elif "Sub" in rightside:
		if "Sub32" in rightside or "Sub64" in rightside:
			target = rightside.partition('(')[-1].rpartition(',')[0]
			target2 = rightside.partition(',')[-1].rpartition(')')[0][2:]
			if '0x' in target2:
				target2 = struct.unpack('>i', rightside.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
			var = leftside.strip()
			#print target
			return (var,[target,IRTYPE.Add,target2])

	elif "Shl" in rightside:
		if "Shl32" in rightside or "Shl64" in rightside:
			target = rightside.partition('(')[-1].rpartition(',')[0]
			target2 = rightside.partition(',')[-1].rpartition(')')[0][2:]
			if '0x' in target2:
				target2 = struct.unpack('>i', rightside.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
			var = leftside.strip()
			#print target
			return (var,[target,IRTYPE.Shl,target2])

	elif "LD" in rightside:
		if "LDle" in rightside:
			target = rightside.partition('(')[-1].rpartition(')')[0]
			var = leftside.strip()
			#print target
			return (var,[target,IRTYPE.LD])

	elif 't' in leftside and ('t' in rightside or '0x' in rightside):
		target = leftside.strip()
		var = rightside.strip()
		#print target
		return (var,[target,IRTYPE.Ass])

## leftside operator ##
	if "PUT" in leftside:
		target = leftside.partition('(')[-1].rpartition(')')[0]
		var = rightside.strip()
		#print target
		return (var,[target,IRTYPE.PUT])

	elif "ST" in leftside:
		if "STle" in side:
			target = side.partition('(')[-1].rpartition(')')[0]
			var = rightside.strip()
			#print target
			return (var,[target,IRTYPE.ST])

## return a tuple (read target, uninitialized) ##
def analysisIR(inst_ir,initList):
	print inst_ir.split('\n')[0]
	filtered = ['if','x86g_calculate_condition','32to1','F32toF64']
	for line in inst_ir.split('\n'):
		print "-----ir start-----"
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
			L,R = __findIRtype(leftside,rightside)
		except:
			error_exit("Err: Found undefined IR Type in \"%s\"" %line)
		print L
		print R
		



	return []
	

	
