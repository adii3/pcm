from PyQt5 import QtWidgets, uic,QtCore
import sys

class Ui2(QtWidgets.QMainWindow):

    switch_window= QtCore.pyqtSignal()

    def openWindow(self):
        self.switch_window.emit()

    def __init__(self):
        super(Ui2, self).__init__()
        uic.loadUi('advanceoptionGui.ui', self)
        self.show()
        #self.setStyleSheet("Ui {background-image: url(); }")
        #self.setStyleSheet("Ui {background-color: brown; }")
        self.Back.clicked.connect(self.openWindow)

if __name__ == "__main__":
    pass
    app = QtWidgets.QApplication(sys.argv)
    window = Ui2()
    app.exec_()


