import os
import random
from crawl import Crawl

class Randomize(Crawl):
    def __init__(self, word, maxImageNum):
        super().__init__(word, maxImageNum)
        
    def randomize_image(self):
        dir_list = []
        
        path = 'crawled_img/' + self.word + '_' + self.maxImageNum
        dir_list = os.listdir(path) # 파일들을 리스트로 
        rand_dir_list = random.sample(dir_list, k=int(self.maxImageNum))
        return rand_dir_list
        
# r = Randomize("dog", "5")
# r.randomize_image()
