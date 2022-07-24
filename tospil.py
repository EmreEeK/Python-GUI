import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from qtt import Ui_Form

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Your code will go here
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.buttonleft.clicked.connect(self.clickedleftbutt)
        self.ui.buttonright.clicked.connect(self.clickedr)
        # Your code ends here
        
        
    
    def clickedleftbutt(self):
        self.ui.label1.setText("you pressed the left button")
    def clickedr(self):
        self.ui.label1.setText("you pressed the right button")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

    