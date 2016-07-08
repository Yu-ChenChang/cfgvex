import unittest
import analysis

def myfun(a):
	c = a + 2
	return c

class UnitTest_1_test(unittest.TestCase):

	def test_assert_raises_myfun(self):
		self.assertEqual(myfun(1),3)

def runtest():
	unittest.main()
