import unittest
import os
from crawl import Crawl
import tempfile

class TestCrawl(unittest.TestCase):
    def setUp(self):
        pass    
        
    def testCrawl(self):
        tmpdir = tempfile.TemporaryDirectory()
        print('임시 디렉토리 생성:', tmpdir.name)
        c1 = Crawl("dog")
        c1.crawl_image(tmpdir.name) # tmpdir에 이미지 30개 크롤링
        tmp_file_list = os.listdir(tmpdir.name)
        self.assertEqual(len(tmp_file_list), 30, msg="이미지 30개 크롤링 성공")
        tmpdir.cleanup()
        
if __name__ == '__main__':
    unittest.main()

