# Copyright 2020
# Nik Fernandez, October 2020
import sys
from PySide2.QtWidgets import *

class Form(QMainWindow):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Before You Kill Yourself")

        layout = QGridLayout()

        feeling_prompt_label = QLabel("How awful do you feel right now?")
        feeling_prompt_input = QLineEdit()
        layout.addWidget(feeling_prompt_label, 0, 0)
        layout.addWidget(feeling_prompt_input, 0, 1)

        # add objects for our layouts
        # first row
        item_label_1 = QLabel(text="Eat a hearty meal.")
        item_checkbox_1 = QCheckBox()
        layout.addWidget(item_label_1, 1, 0)
        layout.addWidget(item_checkbox_1, 1, 1)
        # second row
        item_label_2 = QLabel(text="Drink water.")
        item_checkbox_2 = QCheckBox()
        layout.addWidget(item_label_2, 2, 0)
        layout.addWidget(item_checkbox_2, 2, 1)
        # third row
        item_label_3 = QLabel(text="Pound that caffeine.")
        item_checkbox_3 = QCheckBox()
        layout.addWidget(item_label_3, 3, 0)
        layout.addWidget(item_checkbox_3, 3, 1)
        # row
        item_label_5 = QLabel(text="Listen to your favorite music.")
        item_checkbox_5 = QCheckBox()
        layout.addWidget(item_label_5, 4, 0)
        layout.addWidget(item_checkbox_5, 4, 1)
        # fouth row
        item_label_4 = QLabel(text="Do a little warmup exercise.")
        item_checkbox_4 = QCheckBox()
        layout.addWidget(item_label_4, 5, 0)
        layout.addWidget(item_checkbox_4, 5, 1)

        # set up layout and add items
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

form1 = Form()
form1.show()

# run the application
sys.exit(app.exec_())