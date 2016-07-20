import sys
class resultAnalysis():
	def __init__(self):
		self.addrFuncDic = {}
		self.allFuncAddr = []

		self.unfoundFuncAddr = []
		self.notFuncAddr = []

		self.estFewerFuncAddr = []
		self.estMoreFuncAddr = []
		self.matchedFuncAddr = []

	def update(self, EstDic, TruePairDic):
		for nameAddrPair in TruePairDic:
			## Update addr-func pair dict and all func addr ##
			self.addrFuncDic[nameAddrPair[1]] = nameAddrPair[0]
			self.allFuncAddr += [nameAddrPair[1]]
			## Update unfoundFuncAddr ##
			if nameAddrPair[1] not in EstDic:
				self.unfoundFuncAddr += [nameAddrPair[1]]
			## Update matched, fewer, more funcAddr ##
			else:
				if TruePairDic[nameAddrPair] == EstDic[nameAddrPair[1]]:
					self.matchedFuncAddr += [nameAddrPair[1]]
				elif TruePairDic[nameAddrPair] > EstDic[nameAddrPair[1]]:
					self.estFewerFuncAddr += [nameAddrPair[1]]
				else:
					self.estMoreFuncAddr += [nameAddrPair[1]]

		## Update notFuncAddr ##
		for addr in EstDic:
			if addr not in self.addrFuncDic:
				self.notFuncAddr += [addr]
	def getAllNum(self):
		return len(self.allFuncAddr)

	def getMatchedNum(self):	
		return len(self.matchedFuncAddr)

	def statistic(self):
		accuracy = float(len(self.matchedFuncAddr))/len(self.allFuncAddr)
		print "Accuracy={0:.0f}%".format(accuracy*100)
			
	def printAll(self):
		print "========{:=^30}========".format(' Start Printing Result ')
		sys.stdout.write("------- {:^30} -------\n".format('address and function mapping') + "\t".join(['[%s]:\'%s\'' % (key, value) for (key, value) in sorted(self.addrFuncDic.items(),key=lambda (k,v): int(k,16))]) +'\n') if self.addrFuncDic else ""
		sys.stdout.write("------- {:^30} -------\n".format('all function address') + "\t".join('[%s]' % x for x in sorted(self.allFuncAddr,key=lambda x: int(x,16)))+'\n') if self.allFuncAddr else ""
		sys.stdout.write("------- {:^30} -------\n".format('unfound function address') + "\t".join('[%s]' % x for x in sorted(self.unfoundFuncAddr,key=lambda x: int(x,16)))+'\n') if self.unfoundFuncAddr else ""
		sys.stdout.write("------- {:^30} -------\n".format('found but not function address') + "\t".join('[%s]' % x for x in sorted(self.notFuncAddr,key=lambda x: int(x,16)))+'\n') if self.notFuncAddr else ""
		sys.stdout.write("------- {:^30} -------\n".format('matched function address') + "\t".join('[%s]' % x for x in sorted(self.matchedFuncAddr,key=lambda x: int(x,16)))+'\n') if self.matchedFuncAddr else ""
		sys.stdout.write("------- {:^30} -------\n".format('fewer estimated parameter function address') + "\t".join('[%s]' % x for x in sorted(self.estFewerFuncAddr,key=lambda x: int(x,16)))+'\n') if self.estFewerFuncAddr else ""
		sys.stdout.write("------- {:^30} -------\n".format('more estimated parameter function address') + "\t".join('[%s]' % x for x in sorted(self.estMoreFuncAddr,key=lambda x: int(x,16)))+'\n') if self.estMoreFuncAddr else ""
		print "========{:=^30}========".format(' end ')
