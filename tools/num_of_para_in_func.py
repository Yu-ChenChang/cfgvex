### Print out the VEX IR saved for each instruction ###
import CFG_pb2
import os, sys
from para_finder import *
def error_exit(msg):
	print >> sys.stderr, msg
	exit()

if __name__ == '__main__':
	print "Enter file name: "
	rawFileName = raw_input()
	filename, file_ext = os.path.splitext(rawFileName)
	if file_ext != '.cfg':
		error_exit('File format is not .cfg!')

	infile = file(filename+file_ext,'rb')
	data = infile.read()

	M = CFG_pb2.Module()
	M.ParseFromString(data)
	finder = paraFinder()
	for func in M.internal_funcs:
		finder.parseFromFunc(func)
		print "Entry address of function: " + hex(func.entry_address) + " , the number of parameter = " + str(finder.getParaNum())
		break
					
	infile.close()
	del infile
