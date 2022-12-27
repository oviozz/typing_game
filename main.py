
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QWidget, QListWidget
from typing_functions import Paragraph
import time
import keyboard



class MyWidget(QWidget):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.close()


class Ui_background_main(object):
    def setupUi(self, background_main):
        background_main.setObjectName("background_main")
        background_main.setFixedSize(843, 324)
        background_main.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(background_main)
        self.centralwidget.setObjectName("centralwidget")
        self.white_background = QtWidgets.QLabel(self.centralwidget)
        self.white_background.setGeometry(QtCore.QRect(10, 10, 821, 291))
        self.white_background.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 20px;\n"
                                            "border: 1px solid rgb(171, 171, 171);")
        self.white_background.setText("")
        self.white_background.setObjectName("white_background")
        self.paragraph = QtWidgets.QLabel(self.centralwidget)
        self.paragraph.setGeometry(QtCore.QRect(20, 20, 801, 221))
        self.paragraph.setStyleSheet("font: 24 19pt \"Arial\";")
        self.paragraph.setScaledContents(False)
        self.paragraph.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.paragraph.setWordWrap(True)
        self.paragraph.setObjectName("paragraph")
        self.accurary = QtWidgets.QLabel(self.centralwidget)
        self.accurary.setGeometry(QtCore.QRect(20, 250, 151, 41))
        self.accurary.setStyleSheet("font: 14pt \"Arial\";\n"
                                     "")
        self.accurary.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.accurary.setObjectName("accurary")
        self.dash1 = QtWidgets.QLabel(self.centralwidget)
        self.dash1.setGeometry(QtCore.QRect(170, 240, 20, 41))
        self.dash1.setStyleSheet("font: 20pt \"Bradley Hand ITC\";\n"
                                 "color: rgb(171, 171, 171);")
        self.dash1.setWordWrap(True)
        self.dash1.setObjectName("dash1")
        self.dash2 = QtWidgets.QLabel(self.centralwidget)
        self.dash2.setGeometry(QtCore.QRect(170, 270, 20, 21))
        self.dash2.setStyleSheet("font: 20pt \"Bradley Hand ITC\";\n"
                                 "color: rgb(171, 171, 171);")
        self.dash2.setWordWrap(True)
        self.dash2.setObjectName("dash2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 320, 801, 21))
        """self.lineEdit.setStyleSheet("border: none;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "")"""

        self.lineEdit.setFrame(False)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")


        self.mistakes = QtWidgets.QLabel(self.centralwidget)
        self.mistakes.setGeometry(QtCore.QRect(190, 250, 131, 41))
        self.mistakes.setStyleSheet("font: 15pt \"Arial\";\n"
                                    "")
        self.mistakes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mistakes.setObjectName("mistakes")
        self.dash1_2 = QtWidgets.QLabel(self.centralwidget)
        self.dash1_2.setGeometry(QtCore.QRect(310, 240, 20, 41))
        self.dash1_2.setStyleSheet("font: 20pt \"Bradley Hand ITC\";\n"
                                   "color: rgb(171, 171, 171);")
        self.dash1_2.setWordWrap(True)
        self.dash1_2.setObjectName("dash1_2")
        self.dash2_2 = QtWidgets.QLabel(self.centralwidget)
        self.dash2_2.setGeometry(QtCore.QRect(310, 270, 20, 21))
        self.dash2_2.setStyleSheet("font: 20pt \"Bradley Hand ITC\";\n"
                                   "color: rgb(171, 171, 171);")
        self.dash2_2.setWordWrap(True)
        self.dash2_2.setObjectName("dash2_2")
        self.wpm = QtWidgets.QLabel(self.centralwidget)
        self.wpm.setGeometry(QtCore.QRect(330, 250, 131, 41))
        self.wpm.setStyleSheet("font: 15pt \"Arial\";\n"
                               "")
        self.wpm.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.wpm.setObjectName("wpm")
        self.dash2_3 = QtWidgets.QLabel(self.centralwidget)
        self.dash2_3.setGeometry(QtCore.QRect(440, 270, 20, 21))
        self.dash2_3.setStyleSheet("font: 20pt \"Bradley Hand ITC\";\n"
                                   "color: rgb(171, 171, 171);")
        self.dash2_3.setWordWrap(True)
        self.dash2_3.setObjectName("dash2_3")
        self.dash1_3 = QtWidgets.QLabel(self.centralwidget)
        self.dash1_3.setGeometry(QtCore.QRect(440, 240, 20, 41))
        self.dash1_3.setStyleSheet("font: 20pt \"Bradley Hand ITC\";\n"
                                   "color: rgb(171, 171, 171);")
        self.dash1_3.setWordWrap(True)
        self.dash1_3.setObjectName("dash1_3")
        self.word_left = QtWidgets.QLabel(self.centralwidget)
        self.word_left.setGeometry(QtCore.QRect(460, 250, 200, 41))
        self.word_left.setStyleSheet("font: 15pt \"Arial\";\n"
                               "")
        self.word_left.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.word_left.setObjectName("word_left")
        self.tryagain_button = QtWidgets.QPushButton(self.centralwidget)
        self.tryagain_button.setGeometry(QtCore.QRect(680, 250, 131, 41))
        self.tryagain_button.setStyleSheet("QPushButton {\n"
                                           "    background-color: rgb(207, 207, 207);\n"
                                           "    border: 1px solid rgb(230, 230, 230);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(211, 211, 211);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    background-color: rgb(183, 183, 183);\n"
                                           "}\n"
                                           "")
        self.tryagain_button.setAutoDefault(False)
        self.tryagain_button.setDefault(False)
        self.tryagain_button.setFlat(False)
        self.tryagain_button.setObjectName("tryagain_button")
        self.white_background.raise_()
        self.paragraph.raise_()
        self.accurary.raise_()
        self.dash1.raise_()
        self.dash2.raise_()
        self.lineEdit.raise_()
        self.mistakes.raise_()
        self.dash1_2.raise_()
        self.dash2_2.raise_()
        self.wpm.raise_()
        self.dash1_3.raise_()
        self.dash2_3.raise_()
        self.word_left.raise_()
        self.tryagain_button.raise_()
        background_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(background_main)
        QtCore.QMetaObject.connectSlotsByName(background_main)

        cursor = QtGui.QCursor(Qt.BlankCursor)
        self.lineEdit.setCursor(cursor)

        self.lineEdit.textChanged.connect(self.typing_function)
        self.tryagain_button.clicked.connect(self.reset)

        self.startups()

    def retranslateUi(self, background_main):
        _translate = QtCore.QCoreApplication.translate
        background_main.setWindowTitle(_translate("background_main", "Typing Game - made by prajwal"))
        self.dash1.setText(_translate("background_main", "|"))
        self.dash2.setText(_translate("background_main", "|"))
        self.dash1_2.setText(_translate("background_main", "|"))
        self.dash2_2.setText(_translate("background_main", "|"))
        self.dash2_3.setText(_translate("background_main", "|"))
        self.dash1_3.setText(_translate("background_main", "|"))
        self.tryagain_button.setText(_translate("background_main", "Try Again"))

    def startups(self):
        self.start_time = time.time()

        self.writing_generation = Paragraph.file_open()
        self.paragraph.setText(self.writing_generation)

        self.writing = ''
        self.mistake = 0
        self.accurary_count = 0

        self.word_left.setText(f'Word Left: {len(self.writing.split())}/{len(self.writing_generation.split())}')
        self.mistakes.setText("Mistakes: 0")
        self.wpm.setText("WPM: 0")
        self.accurary.setText("Accuracy: 100%")

        self.lineEdit.setFocus()


    def typing_function(self):
        try:
            if self.lineEdit.text()[-1] == self.paragraph.text()[0]:
                self.paragraph.setText(self.paragraph.text()[1:])
                self.writing += self.paragraph.text()[0]

                self.wpm.setText(f'WPM: {len(self.writing.split()) / (time.time() - self.start_time) * 60:.2f}')

            else:
                self.mistake += 1
                self.mistakes.setText(f'Mistakes: {self.mistake}')

            self.accurary_count += 1
            self.word_left.setText(f'Word Left: {len(self.writing.split())}/{len(self.writing_generation.split())}')
            self.accurary.setText(f'Accurary: {(len(self.writing) / self.accurary_count) * 100:.0f}%')

            if not len(self.paragraph.text()) - 1:
                print('resetting')
                self.reset()
        except:
            pass

    def reset(self):
        self.startups()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_main = QtWidgets.QMainWindow()
    ui = Ui_background_main()
    ui.setupUi(background_main)
    background_main.show()
    sys.exit(app.exec_())
