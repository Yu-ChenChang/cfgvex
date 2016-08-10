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
		self.unint_para = []

	def parseFromFunc(self,func):
		for block in func.blocks:
			self.b_status[block.base_address] = False
			self.addr_to_block[block.base_address] = block
		self.analysisBlock(func.blocks[0],['esp','ebp','ebx','edi','esi','rsp','rbp','r12','r13','r14','r15'],{}) ## callee-saved register ##

	def analysisBlock(self,block,initList,typeDict):
		## Initial list saved those registers that is initialized in previous blocks ##
		curList = initList
		## type dict saved the potential type of registers (or memory location ##
		## may change according to the following instructions ##
		curDict = typeDict
		self.b_status[block.base_address] = True
		for inst in block.insts:
			self.analysisInst(inst.vex_ir,curList,curDict)
		for follow_b in block.block_follows:
			if self.b_status[follow_b] == False:
				self.analysisBlock(self.addr_to_block[follow_b],curList,curDict)

	def analysisInst(self,inst_ir,initList,typeDict):
		target = analysisIR(inst_ir,initList,typeDict)
		self.unint_para.extend( x for x in target if x not in self.unint_para)

	def getParaNum(self):
		print self.unint_para
		return len(self.unint_para)

