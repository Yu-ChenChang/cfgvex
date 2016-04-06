import r2pipe
import CFG_pb2

class AbstractBinary(object):
    def __init__(self, filename):
        self.filename = filename
        self.r2 = r2pipe.open(filename)
        self.r2.cmd("aa")
        self.binaryInfo = self.r2.cmdj("iIj")
        self.cfg  = CFG_pb2.Module()

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

    def findFunctions(self):
        # if the binary is not stripped,
        # get the boundaries of functions from the
        # symbol information
        if not isStripped():
            allsyms = r2.cmdj("isj")
            for s in allsyms:
                # TODO: filter out symbols of types other than function
                f = CFG_pb2.Function()
                f.name = s['name']
                f.entry_address = s['vaddr']
                f.size = s['size']
                cfg.internal_funcs.append(f)
            return
        # in other situations, we need to implement them in other ways

    def generateFuncCfg(self, func):
        pass

    def funcArityAnalyse(self, func):
        pass

    def funcArgTypeAnalyse(self, func):
        pass

    def getAllDirectCallOperands(self):
        pass


class X86Binary(AbstractBinary):
    def __init__(self, filename):
        super(AbstractBinaryAnalysis, self).__init__()
