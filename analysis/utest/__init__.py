import unittest
from analysis import analysis
from readelf import program_arity
from resultAnalysis import resultAnalysis

C_PATH = '../testcases/c_func_test/'
C_2_PATH = '../testcases/c++_func_test/'
MATCHED = 0
TOTAL_F = 0
arch86 = '32'
arch64 = '64'

def evaluateResult(EstFuncDic,TrueFuncPairDic):
	result = resultAnalysis()
	result.update(EstFuncDic,TrueFuncPairDic)
	result.printAll()
	global TOTAL_F
	TOTAL_F += result.getAllNum()
	global MATCHED
	MATCHED += result.getMatchedNum()
	print TOTAL_F
	print MATCHED
	
class UnitTest_x86_test(unittest.TestCase):
	def test_assert_equal_x86_simple_clang_O0(self):
		evaluateResult(analysis(C_PATH+'x86/simple_c_func_test-clang-m32-O0_ex.cfg',arch86),
						program_arity(C_PATH+'x86/simple_c_func_test-clang-m32-O0.o'))
	def test_assert_equal_x86_simple_para_clang_O0(self):
		evaluateResult(analysis(C_PATH+'x86/simple_c_para_type_test-clang-m32-O0_ex.cfg',arch86),
						program_arity(C_PATH+'x86/simple_c_para_type_test-clang-m32-O0.o'))

	def test_assert_equal_x86_simple_gcc_O0(self):
		evaluateResult(analysis(C_PATH+'x86/simple_c_func_test-gcc-m32-O0_ex.cfg',arch86),
						program_arity(C_PATH+'x86/simple_c_func_test-gcc-m32-O0.o'))
	def test_assert_equal_x86_indirect_call_test_2_clang_O0(self):
		evaluateResult(analysis(C_PATH+'x86/indirect_call_test_2-clang-m32-O0_ex.cfg',arch86),
						program_arity(C_PATH+'x86/indirect_call_test_2-clang-m32-O0.o'))

class UnitTest_x64_test(unittest.TestCase):
	def test_assert_equal_x64_simple_clang_O0(self):
		evaluateResult(analysis(C_PATH+'x86_64/simple_c_func_test-clang-m64-O0_ex.cfg',arch64),
						program_arity(C_PATH+'x86_64/simple_c_func_test-clang-m64-O0.o'))
	def test_assert_equal_x64_simple_gcc_O0(self):
		evaluateResult(analysis(C_PATH+'x86_64/simple_c_func_test-gcc-m64-O0_ex.cfg',arch64),
						program_arity(C_PATH+'x86_64/simple_c_func_test-gcc-m64-O0.o'))
	def test_assert_equal_x64_simple_para_clang_O0(self):
		evaluateResult(analysis(C_PATH+'x86_64/simple_c_para_type_test-clang-m64-O0_ex.cfg',arch64),
						program_arity(C_PATH+'x86_64/simple_c_para_type_test-clang-m64-O0.o'))

def runtest():
	unittest.main()
