import CFG_pb2
import os
import pyvex
import archinfo
ARCH = archinfo.ArchX86()
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
	out = M.SerializeToString()
	outfile = file(filename+"_ex"+file_ext,'wb')
	outfile.write(out)
	outfile.close()
	del outfile
#print M.internal_funcs[0].blocks[0].insts[0]
