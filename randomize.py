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
        print(random.sample(dir_list, k=int(self.maxImageNum)))
        
r = Randomize("dog", "10")
r.randomize_image()

  
# import os
# import random

# class select :
#     def __init__(self):
#         self.dir_path = "C:\SWP_AD" # 파일의 경로
#         self.count = 0
#         self.images = []
        

#     def randFromFile(self,file_path):
#         for (root, directories, files) in os.walk(self.dir_path): # 폴더 속의 파일이 무엇이 있는지 return
#             for file in files:
#                 if '.png' in file:
#                     self.count += 1
#                     file_path = os.path.join(root, file)
#                     return file_path

#         for _ in range(self.count):
#             self.images.append(file_path)
#             return self.images
            
#         result = random.sample(self.images,2) # 2 개의 이미지 경로를 랜덤하게 뽑아옴

        
        


