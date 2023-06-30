from PyQt5.QtWidgets import QApplication
import sys
sys.path.append("src")
from src import Editor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Editor.MainUI()
    ui.show()
    app.exec_()