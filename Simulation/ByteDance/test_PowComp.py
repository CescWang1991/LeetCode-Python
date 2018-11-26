import unittest
from Simulation.ByteDance.PowCompare import *

class MyTest(unittest.TestCase):

    def test_1(self):
        """test_1"""
        self.assertEqual("=", powComp(2, 4))

    def test_2(self):
        """test_2"""
        self.assertEqual("=", powComp(2, 2))

    def test_3(self):
        """test_3"""
        self.assertEqual("<", powComp(2, 3))

if __name__=='__main__':
    unittest.main()