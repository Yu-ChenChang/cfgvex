import unittest
from analysis import analysis
from readelf import program_arity

C_PATH = '../testcases/c_func_test/'
C_2_PATH = '../testcases/c++_func_test/'
class UnitTest_x86_test(unittest.TestCase):
	def test_assert_equal_x86_simple_clang_O0(self):
		self.assertEqual(analysis(C_PATH+'x86/simple_c_func_test-clang-m32-O0_ex.cfg')[1:],program_arity(C_PATH+'x86/simple_c_func_test-clang-m32-O0.o')[1:])
	def test_assert_equal_x86_simple_gcc_O0(self):
		self.assertEqual(analysis(C_PATH+'x86/simple_c_func_test-gcc-m32-O0_ex.cfg')[1:],program_arity(C_PATH+'x86/simple_c_func_test-gcc-m32-O0.o')[1:])


class UnitTest_x64_test(unittest.TestCase):
	def test_assert_equal_x64_simple_clang_O0(self):
		self.assertEqual(analysis(C_PATH+'x86_64/simple_c_func_test-clang-m64-O0_ex.cfg')[1:],program_arity(C_PATH+'x86_64/simple_c_func_test-clang-m64-O0.o')[1:])
	def test_assert_equal_x64_simple_gcc_O0(self):
		self.assertEqual(analysis(C_PATH+'x86_64/simple_c_func_test-gcc-m64-O0_ex.cfg')[1:],program_arity(C_PATH+'x86_64/simple_c_func_test-gcc-m64-O0.o')[1:])

def runtest():
	unittest.main()
