# Copyright 2020
# Nik Fernandez, October 2020
import sys
from PySide2.QtWidgets import QApplication
from Windows import MainWindow

# main method
if __name__ == "__main__":
    app = QApplication(sys.argv)

    form1 = MainWindow()
    form1.show()

    # run the application
    sys.exit(app.exec_())