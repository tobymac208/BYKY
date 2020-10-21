# Copyright 2020
# Nik Fernandez, October 2020
import sys
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Before You Kill Yourself")

        layout = QGridLayout()

        # prompt the user to see how they're doing
        feeling_prompt_label = QLabel("How awful do you feel right now?")
        feeling_prompt_box = QComboBox()
        feelings = ["Suicidal", "What's the point?", "Life is boring.", "No one understands.", "This app isn't helpful."]
        feeling_prompt_box.addItems(feelings)
        layout.addWidget(feeling_prompt_label, 0, 0)
        layout.addWidget(feeling_prompt_box, 0, 1)

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
        # fourth row
        item_label_4 = QLabel(text="Do a little warmup exercise.")
        item_checkbox_4 = QCheckBox()
        layout.addWidget(item_label_4, 5, 0)
        layout.addWidget(item_checkbox_4, 5, 1)

        # set up layout and add items
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

# main method
if __name__ == "__main__":
    app = QApplication(sys.argv)

    form1 = MainWindow()
    form1.show()

    # run the application
    sys.exit(app.exec_())