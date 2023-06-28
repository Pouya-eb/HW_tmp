import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, QLineEdit, QLCDNumber
from PyQt5.QtCore import QBasicTimer
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


## make it better with QDesigner


class App(QWidget):
    def __init__(self):
        super().__init__()

        # self.setGeometry(100, 100, 500, 500)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.resize(300, 100)
        self.progressBar.hide()

        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(30, 80)
        self.btnStart.clicked.connect(self.start)

        self.btnResume = QPushButton('Resume', self)
        # self.btnResume.resize(100, 200)
        self.btnResume.move(30, 100)
        self.btnResume.clicked.connect(self.resume)
        self.btnResume.hide()

        self.btnPause = QPushButton('Pause', self)
        self.btnPause.move(30, 120)
        self.btnPause.clicked.connect(self.pause)
        self.btnPause.hide()

        self.timer = QBasicTimer()
        self.step = 0
        
        self.textbox = QLineEdit(self)
        self.textbox.move(300, 300)
        self.textbox.resize(280,40)

        self.btnSetTimer = QPushButton('Set Timer', self)
        self.btnSetTimer.move(30, 140)
        self.btnSetTimer.clicked.connect(self.set)

        self.totalTime = 100;

        self.lcd = QLCDNumber(self)
        self.lcd.move(0, 0)
        self.lcd.resize(100, 100)


    def set(self):
        textboxValue = int(self.textbox.text())
        self.totalTime = textboxValue * 10
        return

    def start(self):
        self.step = 0
        self.progressBar.setValue(0)
        self.progressBar.show()
        self.btnResume.show()
        self.btnPause.show()
        self.resume()

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()

    def resume(self):
        self.timer.start(self.totalTime, self)
    
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.progressBar.hide()
            return

        self.step += 1
        self.progressBar.setValue(self.step)
        self.lcd.display(self.step)

    def mousePressEvent(self, event):
        if event.button() == 1:
            
            cursor = QCursor()
            curserPos = cursor.pos()
            curserX = curserPos.x()
            curserY = curserPos.y()

            windowPos =  self.pos()
            windowX = windowPos.x()
            windowY = windowPos.y()

            lcdPos = self.lcd.size()
            lcdX = lcdPos.width()
            lcdY = lcdPos.height()


            ## in matplotlib x-y
            # if(self.x > 0 and self.y > 0):
            self.start()
            self.lcd.move(curserX - windowX - int(lcdX/2), curserY - windowY - int(lcdY/2))
                # print("Cursor position:", pos.x() , pos.y())
                # print("** : " , self.xWindow, self.yWindow)
                # print(self.lcd.size())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = App()
    demo.show()

    sys.exit(app.exec_())