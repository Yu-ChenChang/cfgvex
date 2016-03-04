import CFG_pb2
import os, sys
from IR_analysis import *
def error_exit(msg):
	print >> sys.stderr, msg
	exit()

class paraFinder:
	def __init__(self):
		self.b_status = {}
		self.addr_to_block = {}
		self.num_of_para = 0

	def parseFromFunc(self,func):
		for block in func.blocks:
				self.b_status[block.base_address] = False
				self.addr_to_block[block.base_address] = block
		self.analysisBlock(func.blocks[0],[])

	def analysisBlock(self,block,initList):
		curList = initList
		self.b_status[block.base_address] = True
		for inst in block.insts:
				self.analysisInst(inst.vex_ir,curList)
		for follow_b in block.block_follows:
				if self.b_status[follow_b] == False:
						self.analysisBlock(self.addr_to_block[follow_b],curList)

	def analysisInst(self,inst_ir,initList):
		target,uniflag = analysisIR(inst_ir)

	def getParaNum(self):
		return self.num_of_para

