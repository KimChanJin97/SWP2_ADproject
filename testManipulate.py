import unittest
from PIL import Image
import random as rd

class testManipulate(unittest.TestCase):
    def setUp(self):
        main_testimg1 = '1.jpg'
        main_testimg2 = '2.jpg'
        self.m1 = Image.open(main_testimg1)
        self.m2 = Image.open(main_testimg2)

    def testMainResizing1(self):
        wsize = self.m1.size[0]
        hsize = self.m1.size[1]
        self.assertTrue(wsize > hsize)

    def testMainResizing2(self):
        wsize = self.m2.size[0]
        hsize = self.m2.size[1]
        self.assertTrue(hsize > wsize)

    def testManipulat1(self):
        wsize = self.m1.size[0]
        hsize = self.m1.size[1]
        x = rd.randint(0, wsize)
        y = rd.randint(0, hsize)
        self.assertTrue(x >= 0 and x <= wsize and y >= 0 and y <= hsize)

    def testManipulat2(self):
        wsize = self.m2.size[0]
        hsize = self.m2.size[1]
        x = rd.randint(0, wsize)
        y = rd.randint(0, hsize)
        self.assertTrue(x >= 0 and x <= wsize and y >= 0 and y <= hsize)

if __name__ == '__main__':
    unittest.main()