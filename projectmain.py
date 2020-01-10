from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import project

class markscalc(QtGui.QMainWindow, project.Ui_MainWindow):
        def __init__(self):
                super(self.__class__,self).__init__()
                self.setupUi(self)
                self.Avg_button.clicked.connect(self.calculatemarks)
        def calculatemarks(self):
                maths = int(self.marks_maths.toPlainText())
                ##print("Maths",maths)
                science = int(self.marks_sci.toPlainText())
                ##print("Sci",science)
                phy = int(self.marks_phy.toPlainText())
                chem = int(self.marks_chem.toPlainText())
                eng = int(self.marks_eng.toPlainText())
                total_marks = int(maths+science+phy+chem+eng)
                print("total marks ",total_marks)
                Average=float(total_marks/5)
                print("Average ",Average)
                Avg_string = " " + str(Average)
                self.total_result.setText(Avg_string)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = markscalc()
	window.show()
	sys.exit(app.exec_())

