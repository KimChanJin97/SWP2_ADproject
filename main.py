from collageGUI import InputWindow
# from crawl import Crawl
# from randmoize import randomize
from PyQt5 import QtWidgets
import sys
import tempfile

def generateCollage(words: list, count: int):
    # 임시 폴더 경로 객체, 문자열 아님
    # 다른 함수에 매개변수로 전달할 때 반드시 문자열인 tempDirPath.name으로 전달해줄 것
    tempDirPath = tempfile.TemporaryDirectory()

    try:        
        count = int(count)
    except:
        pass
    
    tempDirPath.cleanup()




app = QtWidgets.QApplication(sys.argv)

mainWindow = InputWindow()
mainWindow.show()
mainWindow.startButton.clicked.connect(lambda: generateCollage())


# generateCollage()


sys.exit(app.exec_())