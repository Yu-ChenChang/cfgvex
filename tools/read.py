### Print out the VEX IR saved for each instruction ###
import CFG_pb2
import os
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
	for func in M.internal_funcs:
		for block in func.blocks:
			for inst in block.insts:
				if len(inst.vex_ir) != 0:
					print inst.vex_ir
	infile.close()
	del infile
