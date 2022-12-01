from PIL import Image
import random as rd

class Manipulation():
    def __init__(self, mainImg, subImgList):
        self.mainImg = Image.open(mainImg)
        self.subImgList = subImgList
        self.resizing_subImg_List = []
        self.resizing()
        self.manipulat()
        self.saveImg()
        self.showImg()


    def resizing(self):
        for i in range(len(self.subImgList)):
            subImg = Image.open(str(self.subImgList[i]))
            resizeSubImg = subImg.resize((60, 60))
            self.resizing_subImg_List.append(resizeSubImg)

        print(self.resizing_subImg_List)


    def manipulat(self):
        for i in range(len(self.resizing_subImg_List)):
            x = rd.randint(0, 500)
            y = rd.randint(0, 400)
            self.mainImg.paste(self.resizing_subImg_List[i], (x, y), self.resizing_subImg_List[i])

    def saveImg(self):
        self.mainImg.save('result.jpg')
        # main_img.save('절대경로', 'result.jpg')

    def showImg(self):
        self.mainImg.show()

if __name__ == '__main__':
    a = "1.jpg"
    b = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']
    c = Manipulation(a, b)
