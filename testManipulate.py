import unittest
import os
from manipulate import manipulation
from PIL import Image
import random as rd

class testManipulation(unittest.TestCase):
    def setUp(self):
        main_testimg1 = '1.jpg'
        main_testimg2 = '3.jpg'
        sub_testimg = ['4.png']
        self.m1 = Manipulation(main_testimg1, sub_testimg)
        self.m2 = Manipulation(main_testimg2, sub_testimg)

    def testMainResizing1(self):
        wsize = self.m1.mainImg.size[0]
        hsize = self.m1.mainImg.size[1]
        self.assertTrue(wsize > hsize)

    def testMainResizing2(self):
        wsize = self.m2.mainImg.size[0]
        hsize = self.m2.mainImg.size[1]
        self.assertTrue(hsize > wsize)

    def testManipulat1(self):
        wsize = self.m1.mainImg.size[0]
        hsize = self.m1.mainImg.size[1]
        x = rd.randint(0, wsize)
        y = rd.randint(0, hsize)
        self.assertTrue(x >= 0 and x <= wsize and y >= 0 and y <= hsize)

    def testManipulat2(self):
        wsize = self.m2.mainImg.size[0]
        hsize = self.m2.mainImg.size[1]
        x = rd.randint(0, wsize)
        y = rd.randint(0, hsize)
        self.assertTrue(x >= 0 and x <= wsize and y >= 0 and y <= hsize)