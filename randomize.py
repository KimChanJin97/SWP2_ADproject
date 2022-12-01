import os
import random
from crawl import Crawl

def randomize(image_list, num):
    rand_dir_list = random.sample(image_list, k=int(num))
    return rand_dir_list
        

# print(randomize(["a","b","c"], 2))