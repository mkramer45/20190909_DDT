import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
	def __init__(self):
		super(MainPage, self).__init__()
		loadUi('DDTTextGen.ui', self)
		#attaching a function to a button
		self.pushButton.clicked.connect(self.retrieveText)

	def retrieveText(self):
		words = self.plainTextEdit.toPlainText()

		all_uppercase = words.upper()
		final_output = all_uppercase.replace('I', 'i')

		self.textEdit.setText(final_output)


app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())


