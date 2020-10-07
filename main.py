from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys
app = QApplication()
ventana = MainWindow()
ventana.show()

sys.exit(app.exec_())

# pyside2-uic mainwindow.ui > ui_mainwindow.py

