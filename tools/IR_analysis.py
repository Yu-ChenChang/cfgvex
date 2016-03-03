import CFG_pb2
import os, sys
def error_exit(msg):
	print >> sys.stderr, msg
	exit()

class paraFinder:
	def __init__(self,regList,stackList):
		self.regList = regList
		self.stackList = stackList
		self.b_status = {}
		self.addr_to_block = {}
		self.num_of_para = 0
	def	parseFromFunc(self,func):
		for block in func.blocks:
			self.b_status[block.base_address] = False
			self.addr_to_block[block.base_address] = block

		self.analysisBlock(func.blocks[0])

	def analysisBlock(self,block):
		self.b_status[block.base_address] = True
		for inst in block.insts:
			self.analysisInst(inst.vex_ir)
		for follow_b in block.block_follows:
			if self.b_status[follow_b] == False:
				self.analysisBlock(self.addr_to_block[follow_b])
		
	def	analysisInst(self,inst_ir):
		print inst_ir
	
	def getParaNum(self):
		return self.num_of_para
	
