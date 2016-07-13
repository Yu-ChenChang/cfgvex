### Print out the VEX IR saved for each instruction ###
import CFG_pb2
import os, sys
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
		#print hex(func.entry_address)
		for block in func.blocks:
			if (block.insts[0].inst_bytes).encode('hex') == '55':
				print "----block----"
				for inst in block.insts:
					print (inst.inst_bytes).encode('hex')
				print "-------------\n"
					
	infile.close()
	del infile
