from collageGUI import InputWindow
from PyQt5 import QtWidgets
from crawl import Crawl
from randomize import randomize
from manipulate import manipulate
import sys
import tempfile


def generateCollage(mainImgPath: str, words: list, count: int):
    # 임시 폴더 경로 객체, 문자열 아님
    # 다른 함수에 매개변수로 전달할 때 반드시 문자열인 tempDirPath.name으로 전달해줄 것
    with tempfile.TemporaryDirectory() as tempDirPath:
        crawl = Crawl(words)
        manipulate(mainImgPath, randomize(crawl.crawl_image(tempDirPath), count))


app = QtWidgets.QApplication(sys.argv)

mainWindow = InputWindow()
mainWindow.show()
mainWindow.startButton.clicked.connect(lambda: generateCollage(mainWindow.imageLineEdit.text(), mainWindow.keywordLineEdit.text(), int(mainWindow.maxImageNumLineEdit.currentText())))

sys.exit(app.exec_())