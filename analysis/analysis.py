### Print out the VEX IR saved for each instruction ###
import CFG_pb2
import os, sys
from parafinder import *
def error_exit(msg):
	print >> sys.stderr, msg
	exit()

#if __name__ == '__main__':
def analysis(rawFileName,arch):
	filename, file_ext = os.path.splitext(rawFileName)
	if file_ext != '.cfg':
		error_exit('File format is not .cfg!')

	infile = file(filename+file_ext,'rb')
	data = infile.read()

	M = CFG_pb2.Module()
	M.ParseFromString(data)
	res = {}
	for i,func in enumerate(M.internal_funcs):
			finder = paraFinder(arch)
			finder.parseFromFunc(func)
			print "Entry address of function: " + hex(func.entry_address) + " , the number of parameter = " + str(finder.getParaNum())
			res[hex(func.entry_address).rstrip('L')] = [finder.getParaNum()]
					
	infile.close()
	del infile
	return res
