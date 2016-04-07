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
        if not self.isStripped():
            print  self.filename + " not stripped"
            allsyms = self.r2.cmdj("isj")
            for s in allsyms:
                if s['type'] == 'FUNC':
                    f = CFG_pb2.Function()
                    f.name = s['name']
                    f.entry_address = s['vaddr']
                    f.size = s['size']
                    f.arity = -1    # mark it as unknown
                    self.cfg.internal_funcs.extend([f])
                else:
                    # symbol is not a function, skip
                    pass
        else:
            # under other situations, we need to implement them in other ways
            pass


    def generateFuncCfg(self, func):
        self.r2.cmd("s " + str(func.entry_address))
        self.r2.cmd("af")
        # it only returns one object
        cfgmeta = self.r2.cmdj("agj")
        if cfgmeta and len(cfgmeta) != 0:
            if len(cfgmeta) > 1:
                print "[warning]the length of cfgmeta is greater than 1"
            cfgmeta0 = cfgmeta[0]
            func.arity = cfgmeta0['nargs']
            for b in cfgmeta0['blocks']:
                # add blocks to the function
                pass
        else:
            print "[ERROR] could not generate cfg for function " + func.name

    def doAllAnalysis(self):
        self.findFunctions()

        for f in self.cfg.internal_funcs:
            self.funcArityAnalyse(f)
            # funcArgTypeAnalyse(f)
            self.generateFuncCfg(f)

    def funcArityAnalyse(self, func):
        pass

    def funcArgTypeAnalyse(self, func):
        pass

    def getAllDirectCallOperands(self):
        pass

    def getFuncArityInfo(self):
        ret = []
        for f in self.cfg.internal_funcs:
            f_info = {}
            f_info['name'] = f.name
            f_info['arity'] = f.arity
            ret.append(f_info)

        return ret

class X86Binary(AbstractBinary):
    def __init__(self, filename):
        super(AbstractBinaryAnalysis, self).__init__()
