import sys
from PySide2.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Sample")

        # add objects for layout
        edit = QLineEdit("What's your name?")
        label = QLabel(text="Hello")
        checkbox = QCheckBox()

        # set up layout and add items
        layout = QVBoxLayout()
        layout.addWidget(edit)
        layout.addWidget(label)
        layout.addWidget(checkbox)

        self.setLayout(layout)

app = QApplication(sys.argv)

form1 = Form()
form1.show()

# run the application
sys.exit(app.exec_())