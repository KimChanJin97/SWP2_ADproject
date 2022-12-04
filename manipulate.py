from PIL import Image
import random as rd

class manipulate():
    def __init__(self, mainImg, subImgList):
        self.mainImg = Image.open(mainImg)
        self.subImgList = subImgList
        self.resizing_subImg_List = []
        self.mainResizing()
        self.subResizing()
        self.manipulat()
        self.saveImg()
        self.showImg()
        
    def subResizing(self):
        for i in range(len(self.subImgList)):
            subImg = Image.open(str(self.subImgList[i]))
            resizeSubImg = subImg.resize((60, 60))
            self.resizing_subImg_List.append(resizeSubImg)
    
    def mainResizing(self):
        size = 500
        if self.mainImg.size[0] > self.mainImg.size[1]:
            tempsize = self.mainImg.size[0]
        else:
            tempsize = self.mainImg.size[1]
        
        percent = size/tempsize
        self.wsize = int(self.mainImg.size[0]*percent)
        self.hsize = int(self.mainImg.size[1]*percent)

        self.mainImg = self.mainImg.resize((self.wsize, self.hsize))


    def manipulat(self):
        for i in range(len(self.resizing_subImg_List)):
            x = rd.randint(0, (self.wsize-50))
            y = rd.randint(0, (self.hsize-50))
            self.mainImg.paste(self.resizing_subImg_List[i], (x, y), self.resizing_subImg_List[i])

    def saveImg(self):
        self.mainImg.save('result.jpg')
        # main_img.save('절대경로', 'result.jpg')

    def showImg(self):
        self.mainImg.show()