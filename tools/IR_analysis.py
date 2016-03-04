import CFG_pb2
import os, sys
import struct
def error_exit(msg):
	print >> sys.stderr, msg
	exit()

## enum of IR type ##
class IRTYPE:
	GET, PUT, Add, Sub, Shl, LD, ST = range(7)

def findIRtype(side):
	if "GET" in side:
		if "I32" in side or "I64" in side:
			target = side.partition('(')[-1].rpartition(')')[0]
			#print target
			return [target,IRTYPE.GET]
	
	elif "PUT" in side:
		target = side.partition('(')[-1].rpartition(')')[0]
		#print target
		return [target,IRTYPE.PUT]
	
	elif "Add" in side:
		if "Add32" in side or "Add64" in side:
			target = side.partition('(')[-1].rpartition(',')[0]
			target2 = side.partition(',')[-1].rpartition(')')[0][2:]
			if '0x' in target2:
				target2 = struct.unpack('>i', side.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
			#print target
			return [target,IRTYPE.Add,target2]

	elif "Sub" in side:
		if "Sub32" in side or "Sub64" in side:
			target = side.partition('(')[-1].rpartition(',')[0]
			target2 = side.partition(',')[-1].rpartition(')')[0][2:]
			if '0x' in target2:
				target2 = struct.unpack('>i', side.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
			#print target
			return [target,IRTYPE.Add,target2]

	elif "Shl" in side:
		if "Shl32" in side or "Shl64" in side:
			target = side.partition('(')[-1].rpartition(',')[0]
			target2 = side.partition(',')[-1].rpartition(')')[0][2:]
			if '0x' in target2:
				target2 = struct.unpack('>i', side.partition(',')[-1].rpartition(')')[0][2:].decode('hex'))[0]
			#print target
			return [target,IRTYPE.Shl,target2]

	elif "LD" in side:
		if "LDle" in side:
			target = side.partition('(')[-1].rpartition(')')[0]
			#print target
			return [target,IRTYPE.LD]

	elif "ST" in side:
		if "STle" in side:
			target = side.partition('(')[-1].rpartition(')')[0]
			#print target
			return [target,IRTYPE.ST]

	elif 't' in side.strip(' ') and len(side.strip(' ')) <= len('txx'):
		target = side.strip(' ')
		#print target
		return [target]
	
	elif '0x' in side.strip(' ') and len(side.strip(' ')) <= len('0xffffffff'):
		target = side.strip(' ')
		#print target
		return [target]

## return a tuple (read target, uninitialized) ##
def analysisIR(inst_ir):
	print inst_ir.split('\n')[0]
	filtered = ['if','x86g_calculate_condition','32to1','F32toF64']
	for line in inst_ir.split('\n'):
		print "-----ir start-----"
		filflag = False
		for irst in filtered:
			if irst in line:
				filflag = True
		if filflag:
			continue
		try:
			ind = line.index('=')
		except:
			continue
		leftside = line[:ind]
		rightside = line[ind+1:]
		L = findIRtype(leftside)
		R = findIRtype(rightside)
		if L is None or R is None:
			print line
			error_exit("Err: Found undefined IR Type!")
		print L
		print R



	return (0,True)
	

	
