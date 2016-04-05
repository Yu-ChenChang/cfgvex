import r2pipe
import json

class AbstractBinary(object):
    def __init__(self, filename):
        self.filename = filename
        self.r2 = r2pipe.open(filename)
        self.r2.cmd("aa")
        self.binaryInfo = self.r2.cmdj("iIj")

    def __del__(self):
        if self.r2:
            self.r2.quit()

    def getFileName(self):
        return self.filename;

    def isStripped(self):
        return self.binaryInfo['stripped']

    def getBinaryFormat(self):
        return self.binaryInfo['bintype']

    def getNumOfBits(self):
        return self.binaryInfo['bits']

    def getArch(self):
        return self.binaryInfo['arch']

    def getDataInfo(self):
        pass

    def collectAllFuncInfo(self):
        pass

    def genCfg(self):
        pass

    def funcArityAnalyse(self):
        pass

    def funcArgTypeAnalyse(self):
        pass

    def getAllDirectCallOperands(self):
        pass


class X86Binary(AbstractBinary):
    def __init__(self, filename):
        super(AbstractBinaryAnalysis, self).__init__()
