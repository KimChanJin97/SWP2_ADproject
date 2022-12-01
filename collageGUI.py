import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import sys


class Collage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.image = QtWidgets.QLabel()
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)

        # 이미지 업로드
        imagePathLabel = QtWidgets.QLabel('이미지 업로드 :')
        self.imageLineEdit = QtWidgets.QLineEdit(self)
        self.imageLineEdit.setFixedWidth(240)
        self.imageButton = QtWidgets.QPushButton('Upload', self)
        self.imageButton.clicked.connect(self.imageButtonClicked)
        self.imageButton.setFixedWidth(128)

        # 키워드 입력
        keywordLabel = QtWidgets.QLabel('키워드 입력 :', self)
        self.keywordLineEdit = QtWidgets.QLineEdit(self)
        self.keywordLineEdit.setFixedWidth(240)
        self.keywordButton = QtWidgets.QPushButton('Start')
        self.keywordButton.setFixedWidth(128)
        
        # 이미지 갯수 입력
        maxImageNumLabel = QtWidgets.QLabel('이미지 갯수 입력 :', self)
        self.maxImageNumLineEdit = QtWidgets.QLineEdit(self)
        self.maxImageNumLineEdit.setFixedWidth(240)
        self.maxImageNumButton = QtWidgets.QPushButton('Start')
        self.maxImageNumButton.setFixedWidth(128)
        
        formLayout = QtWidgets.QFormLayout()
        formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        # 이미지 업로드
        formLayout.addRow(imagePathLabel, self.imageLineEdit)
        formLayout.addWidget(self.imageButton)
        # 키워드 입력
        formLayout.addRow(keywordLabel, self.keywordLineEdit)
        formLayout.addWidget(self.keywordButton)
        # 이미지 갯수 입력
        formLayout.addRow(maxImageNumLabel, self.maxImageNumLineEdit)
        formLayout.addWidget(self.maxImageNumButton)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget(self.image)
        self.mainLayout.addLayout(formLayout)

        self.setLayout(self.mainLayout)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('mock-up')
        self.show()
    
    def setImage(self, path: str = ''):
        self.image.setPixmap(QtGui.QPixmap(path).scaled(256, 256, QtCore.Qt.AspectRatioMode.KeepAspectRatio))

    def imageButtonClicked(self):
        filter = 'Image(*.jpg *.bmp *.jpeg *.png)'
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './', filter)[0]
        
        if len(path) == 0:
            return
        
        self.setImage(path)
        self.imageLineEdit.setText(path)