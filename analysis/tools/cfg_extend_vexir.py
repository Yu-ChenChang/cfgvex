import CFG_pb2
import os, sys
import pyvex
import archinfo
ARCH = archinfo.ArchX86()
def error_exit(msg):
	print >> sys.stderr, msg
	exit()
	

if __name__ == '__main__':
	rawFileName = raw_input("Enter file name: \n")
	archNum = raw_input("0 for x86 (default), 1 for x64\n")
	filename, file_ext = os.path.splitext(rawFileName)
	if file_ext != '.cfg':
		error_exit('File format is not .cfg!')
	if archNum == '1':
		ARCH = archinfo.ArchAMD64()
		print "x64 is selected!"

	infile = file(filename+file_ext,'rb')
	data = infile.read()
	infile.close()
	del infile

	M = CFG_pb2.Module()
	M.ParseFromString(data)
	for func in M.internal_funcs:
		for block in func.blocks:
			for inst in block.insts:
				if len(inst.vex_ir) == 0:
					irsb = pyvex.IRSB(inst.inst_bytes, inst.inst_addr, ARCH)
					for stmt in irsb.statements[15:]:
						inst.vex_ir += stmt.__str__()+'\n'
				else:
					error_exit('File already contain VEX IR!')
					
	out = M.SerializeToString()
	outfile = file(filename+"_ex"+file_ext,'wb')
	outfile.write(out)
	outfile.close()
	del outfile
#print M.internal_funcs[0].blocks[0].insts[0]
