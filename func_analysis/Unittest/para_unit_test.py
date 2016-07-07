import unittest
import ../num_of_para_in_func

def myfun(a,b):
    c = a + b
    raise ValueError('invalid args')


class UnitTest_1_test(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True,"AssertTue with given True")

    # Fail
    def test_fail(self):
        self.assertTrue(False,"assertTrue with given False")

    # runtime error
    def test_error(self):
        raise RuntimeError('Test error!',"raise runtimeError")

    def testEqual(self):
        self.assertEqual(2, 2)


    def testNotEqual(self):
        self.assertEqual(2, 3-2)

    def test_assert_raises_myfun(self):
        self.assertRaises(ValueError, myfun, 1, 2)


if __name__ == '__main__':
    unittest.main()
