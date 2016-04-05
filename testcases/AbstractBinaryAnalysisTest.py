#!/usr/bin/python

import unittest

import sys

sys.path.append("../tools")

from AbstractBinaryAnalysis import *

class AbstractBinaryAnalysisTest(unittest.TestCase):
    bfs = ["binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-clang++-m64-O3.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-g++-m64-O2.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-g++-m64-O1.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-clang++-m64-O0.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-clang++-m64-Os.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-g++-m64-O1.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-g++-m64-O1.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-g++-m64-O0.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-clang++-m64-O2.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-clang++-m64-O0.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-clang++-m64-Os.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-g++-m64-Os.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-clang++-m64-O2.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-clang++-m64-O3.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-g++-m64-O3.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-clang++-m64-O2.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-g++-m64-O3.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-g++-m64-O0.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-clang++-m64-O1.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-g++-m64-O3.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-g++-m64-O0.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-clang++-m64-O1.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-clang++-m64-O3.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-g++-m64-O2.o",
           "binaries-for-test/x86_64/c++-func-test/simple_c++_class_test-g++-m64-O2.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-clang++-m64-O1.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-g++-m64-Os.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-clang++-m64-Os.o",
           "binaries-for-test/x86_64/c++-func-test/default-value-arg-func-test-g++-m64-Os.o",
           "binaries-for-test/x86_64/c++-func-test/exception_test-clang++-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-gcc-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-clang-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-clang-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-gcc-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-clang-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-gcc-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-clang-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-clang-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-gcc-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-gcc-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-clang-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-gcc-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-clang-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-clang-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-gcc-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-gcc-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-gcc-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-gcc-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-clang-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-gcc-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-clang-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-gcc-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-gcc-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-clang-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-gcc-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-clang-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-gcc-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-gcc-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-gcc-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-clang-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-clang-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-gcc-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-gcc-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-gcc-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-clang-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-clang-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-clang-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-gcc-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-clang-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-gcc-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-gcc-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-gcc-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-clang-m64-O2.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-clang-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-clang-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-clang-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-clang-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-clang-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-gcc-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-gcc-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-gcc-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_2-clang-m64-Os.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-gcc-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-clang-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-clang-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/simple_c_func_test-clang-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/indirect_call_test_1-gcc-m64-O3.o",
           "binaries-for-test/x86_64/c-func-test/complex_arg_test-gcc-m64-O0.o",
           "binaries-for-test/x86_64/c-func-test/tail-call-test-clang-m64-O1.o",
           "binaries-for-test/x86_64/c-func-test/variadic_func_test-clang-m64-O1.o",
           "binaries-for-test/x86/c++-func-test/exception_test-g++-m32-O2.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-g++-m32-O0.o",
           "binaries-for-test/x86/c++-func-test/exception_test-clang++-m32-O1.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-clang++-m32-O1.o",
           "binaries-for-test/x86/c++-func-test/exception_test-g++-m32-Os.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-g++-m32-O3.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-clang++-m32-Os.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-clang++-m32-Os.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-g++-m32-O1.o",
           "binaries-for-test/x86/c++-func-test/exception_test-g++-m32-O0.o",
           "binaries-for-test/x86/c++-func-test/exception_test-g++-m32-O3.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-clang++-m32-O3.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-g++-m32-O1.o",
           "binaries-for-test/x86/c++-func-test/exception_test-clang++-m32-O3.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-g++-m32-Os.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-clang++-m32-O2.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-clang++-m32-O0.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-clang++-m32-O1.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-g++-m32-O0.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-clang++-m32-O0.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-clang++-m32-O2.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-g++-m32-Os.o",
           "binaries-for-test/x86/c++-func-test/exception_test-clang++-m32-O2.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-g++-m32-O3.o",
           "binaries-for-test/x86/c++-func-test/exception_test-g++-m32-O1.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-g++-m32-O2.o",
           "binaries-for-test/x86/c++-func-test/simple_c++_class_test-g++-m32-O2.o",
           "binaries-for-test/x86/c++-func-test/exception_test-clang++-m32-Os.o",
           "binaries-for-test/x86/c++-func-test/exception_test-clang++-m32-O0.o",
           "binaries-for-test/x86/c++-func-test/default-value-arg-func-test-clang++-m32-O3.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-gcc-m32-Os.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-clang-m32-Os.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-clang-m32-O2.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-clang-m32-Os.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-clang-m32-O3.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-gcc-m32-O0.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-clang-m32-O1.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-clang-m32-Os.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-gcc-m32-O0.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-gcc-m32-O2.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-clang-m32-O1.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-gcc-m32-Os.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-clang-m32-O0.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-clang-m32-O2.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-gcc-m32-O2.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-clang-m32-O3.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-gcc-m32-O1.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-clang-m32-O0.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-clang-m32-O0.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-clang-m32-O2.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-clang-m32-O3.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-gcc-m32-Os.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-gcc-m32-O0.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-gcc-m32-O2.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-gcc-m32-O0.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-gcc-m32-O1.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-clang-m32-O3.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-gcc-m32-O1.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-clang-m32-O3.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-gcc-m32-Os.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-gcc-m32-O3.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-clang-m32-Os.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-gcc-m32-O3.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-gcc-m32-O2.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-gcc-m32-Os.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-gcc-m32-O3.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-clang-m32-Os.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-gcc-m32-O1.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-gcc-m32-O3.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-clang-m32-O1.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-gcc-m32-O3.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-clang-m32-O0.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-clang-m32-O3.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-clang-m32-O1.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-clang-m32-Os.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-gcc-m32-O0.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-clang-m32-O2.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-clang-m32-O0.o",
           "binaries-for-test/x86/c-func-test/simple_c_func_test-gcc-m32-O0.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-clang-m32-O0.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-gcc-m32-O3.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-clang-m32-O2.o",
           "binaries-for-test/x86/c-func-test/complex_arg_test-gcc-m32-O2.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-clang-m32-O1.o",
           "binaries-for-test/x86/c-func-test/tail-call-test-gcc-m32-O1.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-gcc-m32-Os.o",
           "binaries-for-test/x86/c-func-test/variadic_func_test-gcc-m32-O2.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_1-gcc-m32-O1.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-clang-m32-O1.o",
           "binaries-for-test/x86/c-func-test/indirect_call_test_2-clang-m32-O2.o"
    ]

    def test_isStripped(self):
        for bf in AbstractBinaryAnalysisTest.bfs:
            aba = AbstractBinary(bf)
            self.assertFalse(aba.isStripped())
            del aba

    def test_getBinaryFormat(self):
        for bf in AbstractBinaryAnalysisTest.bfs:
            aba = AbstractBinary(bf)
            self.assertEqual(aba.getBinaryFormat(), "elf")
            del aba

    def test_getNumOfBits(self):
        for bf in AbstractBinaryAnalysisTest.bfs:
            aba = AbstractBinary(bf)
            if aba.getFileName().find("64") == -1:
                self.assertEqual(aba.getNumOfBits(), 32)
            else:
                self.assertEqual(aba.getNumOfBits(), 64)

            del aba

    def test_getArch(self):
         for bf in AbstractBinaryAnalysisTest.bfs:
             aba = AbstractBinary(bf)
             self.assertEqual(aba.getArch(), "x86");
             del aba

    def test_comprehensive(self):
        for bf in AbstractBinaryAnalysisTest.bfs:
            aba = AbstractBinary(bf)
            self.assertFalse(aba.isStripped())
            self.assertEqual(aba.getBinaryFormat(), "elf")

            if aba.getFileName().find("64") == -1:
                self.assertEqual(aba.getNumOfBits(), 32)
            else:
                self.assertEqual(aba.getNumOfBits(), 64)

            self.assertEqual(aba.getArch(), "x86")

            del aba

if __name__ == '__main__':
    unittest.main()
