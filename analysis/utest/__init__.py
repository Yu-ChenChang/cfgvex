import unittest
from analysis import analysis

class UnitTest_1_test(unittest.TestCase):

	def test_assert_equal_1(self):
		self.assertEqual(analysis('cfg_2_ex.cfg'),1)

def runtest():
	unittest.main()
