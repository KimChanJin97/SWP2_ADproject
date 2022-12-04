import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

class InputWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.__image = QtWidgets.QLabel()
        self.__image.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop)

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
        
        # 이미지 갯수 입력
        maxImageNumLabel = QtWidgets.QLabel('이미지 갯수 입력 :', self)
        self.maxImageNumLineEdit = QtWidgets.QComboBox(self)
        self.maxImageNumLineEdit.setFixedWidth(240)
        for i in range(1, 30):
            self.maxImageNumLineEdit.addItem(f'{i}')

        # 콜라주 생성
        self.startButton = QtWidgets.QPushButton('Start')
        self.startButton.setFixedWidth(128)
        
        formLayout = QtWidgets.QFormLayout()
        formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        # 이미지 업로드
        formLayout.addRow(imagePathLabel, self.imageLineEdit)
        formLayout.addWidget(self.imageButton)
        # 키워드 입력
        formLayout.addRow(keywordLabel, self.keywordLineEdit)
        # 이미지 갯수 입력
        formLayout.addRow(maxImageNumLabel, self.maxImageNumLineEdit)
        # 콜라주 생성
        formLayout.addWidget(self.startButton)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mainLayout.addWidget(self.__image)
        self.mainLayout.addLayout(formLayout)

        self.setLayout(self.mainLayout)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('main')
    
    def setImage(self, path: str = ''):
        self.__image.setPixmap(QtGui.QPixmap(path).scaled(256, 256, QtCore.Qt.AspectRatioMode.KeepAspectRatio))

    def imageButtonClicked(self):
        filter = 'Image(*.jpg *.bmp *.jpeg *.png)'
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './', filter)[0]
        
        if len(path) == 0:
            return
        
        self.setImage(path)
        self.imageLineEdit.setText(path)