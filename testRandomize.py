import unittest
from randomize import randomize

class TestRandomize(unittest.TestCase):
    
    def setUp(self):
        self.list1 = ["a/1.png"]
        self.list26 = self.list1 + ["b/2.png","c/3.png","d/4.png","e/5.png","f/6.png","g/7.png","h/8.png","i/9.png", "j/10.png",
                  "k/11.png","l/12.png","m/13.png","n/14.png","o/15.png","p/16.png","q/17.png","r/18.png","s/19.png","t/20.png",
                  "u/21.png","v/22.png","w/23.png","x/24.png","y/25.png","z/26.png"]
        self.basicList = self.list26 + ["aa/27.png", "bb/28.png", "cc/29.png", "dd/30.png"] # 크롤링 30개 고정
        self.list30 = self.basicList
        
 
    # 크롤링할 이미지는 30개 고정, 무작위 추출 갯수를 1개로 지정할 경우
    def testRand1(self):
        rand1list = randomize(self.basicList, 1)
        for i in rand1list:
            self.assertIn(i, self.basicList, msg="1 file is in basicList")
        
    # 크롤링할 이미지는 30개 고정, 무작위 추출 갯수를 26개로 지정할 경우
    def testRand26(self):
        rand26list = randomize(self.basicList, 26)
        for i in rand26list:
            self.assertIn(i, self.basicList, msg="26 files are in basicList") 
        
    # 크롤링할 이미지는 30개 고정, 무작위 추출 갯수를 35개로 지정할 경우 에러 발생!!!
    # def testRand35(self):
    #     rand35list = randomize(self.basicList, 35)
    #     for i in rand35list:
    #         self.assertIn(i, self.basicList, msg="35 files are in basicList")
        
if __name__ == '__main__':
    unittest.main()       

