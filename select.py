import os
import random

dir_path = "C:\SWP_AD" # 파일의 경로

count = 0
images = []
for (root, directories, files) in os.walk(dir_path): # 폴더 속의 파일이 무엇이 있는지 return
    for file in files:
        if '.png' in file:
            count += 1
            file_path = os.path.join(root, file)
            print(file_path)

for _ in range(count):
    images.append(file_path)
print(images)

r = random.randrange(count)
print(images[r])



