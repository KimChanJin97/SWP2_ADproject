import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import sys


class MainCollage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.image = QtWidgets.QLabel()
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)

        imagePathLabel = QtWidgets.QLabel('이미지 업로드 :')
        self.imageLineEdit = QtWidgets.QLineEdit(self)
        self.imageLineEdit.setFixedWidth(240)
        self.imageButton = QtWidgets.QPushButton('Upload', self)
        self.imageButton.clicked.connect(self.imageButtonClicked)
        self.imageButton.setFixedWidth(128)

        keywordLabel = QtWidgets.QLabel('키워드 입력 :', self)
        self.keywordLineEdit = QtWidgets.QLineEdit(self)
        self.keywordLineEdit.setFixedWidth(240)
        self.keywordButton = QtWidgets.QPushButton('Start')
        self.keywordButton.setFixedWidth(128)
        # self.keywordButton.clicked.connect()
        
        formLayout = QtWidgets.QFormLayout()
        formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        formLayout.addRow(imagePathLabel, self.imageLineEdit)
        formLayout.addWidget(self.imageButton)
        formLayout.addRow(keywordLabel, self.keywordLineEdit)
        formLayout.addWidget(self.keywordButton)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget(self.image)
        self.mainLayout.addLayout(formLayout)

        self.setLayout(self.mainLayout)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('mock-up')
        self.show()

        someClass = SomeClass()

        someClass.request("REQUEST")

        self.setImage()
    
    def setImage(self, path: str = ''):
        self.image.setPixmap(QtGui.QPixmap(path).scaled(256, 256, QtCore.Qt.AspectRatioMode.KeepAspectRatio))

    def imageButtonClicked(self):
        filter = 'Image(*.jpg *.bmp *.jpeg *.png)'
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './', filter)[0]

        # 업로드 취소 시 path가 빈 문자열로 들어옴
        # 그냥 예외 때려?
        if len(path) == 0:
            return
        
        self.setImage(path)
        self.imageLineEdit.setText(path)
    
class SomeClass():
    def request(self, str):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    collage = MainCollage()
    sys.exit(app.exec_())
