import os.path
import syntax_python
import  syntax_cpp
from PyQt5.QtWidgets import *
from PyQt5.uic import *
import  re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import *
import sys
import os.path

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI,self).__init__()
        #QMainWindow.__init__(self)
        loadUi("src/EditorUi.ui" , self)
        self.actionOpen.triggered.connect(self.OpenPressed)
        self.create_toolbar()
        self.setWindowIcon(QIcon('src/Resources/icon.png'))
        self.ok=True

        self.current_path = None
        self.current_fontsize = 8
        self.setWindowTitle("src/Untitled")
        self.setCentralWidget(self.textEdit)

        # self.actionNew.set
        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave_As_PDF.triggered.connect(self.save_as_pdf)
        self.actioncolor.triggered.connect(self.color)
        self.actionfont.triggered.connect(self.font_)
        self.actionpython.triggered.connect(self.python)
        self.actionc.triggered.connect(self.cpp)
        self.actionundo.triggered.connect(self.textEdit.undo)
        self.actionredo.triggered.connect(self.textEdit.redo)
        self.actioncut.triggered.connect(self.textEdit.cut)
        self.actionPaste.triggered.connect(self.textEdit.paste)
        self.actionCopy.triggered.connect(self.textEdit.copy)
        self.actionClose_2.triggered.connect(QCoreApplication.instance().quit)
        self.actioninsert_image.triggered.connect(self.addimage)
        self.actiondefault.triggered.connect(self.defaut)
        self.actionClear.triggered.connect(self.textEdit.clear)
        self.actionMinimize.triggered.connect(lambda : self.showMinimized())
        self.actionNormalScreen.triggered.connect(lambda : self.showNormal())
        self.actionFullScreen.triggered.connect(lambda : self.showFullScreen())
        

    def dragEnterEvent(self, event):
        print("this is here")
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        print("this is here")
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        print("this is here")
        try:
            if event.mimeData().hasImage:
                event.setDropAction(Qt.CopyAction)
                file_path = event.mimeData().urls()[0].toLocalFile()
                # self.set_path(file_path)
                print(f"file_path")
                cursor = QTextCursor(self.textEdit.document())
                p1 = cursor.position()

                cursor.insertImage(file_path)

                event.accept()
            else:
                event.ignore()
        except Exception as e:
            print(e)

    def newFile(self):
        ui2=MainUI()

        ui2.textEdit.clear()
        ui2.setWindowTitle("Untitled")
        ui2.current_path = None
        # print("new file")
        ui2.show()

    def saveFile(self):
        if self.current_path is None:
            # save the changes without opening dialog
            self.saveFileAs()

        filetext = self.textEdit.toPlainText()
        try:
            with open(self.current_path, 'w') as f:
                f.write(filetext)

        except Exception as e:
            print(e)


    def saveFileAs(self):
        pathname = QFileDialog.getSaveFileName(self, 'Save file', 'D:\codefirst.io\PyQt5 Text Editor', 'Text files(*.txt)')
        filetext = self.textEdit.toPlainText()
        try:
            with open(pathname[0], 'w') as f:
                f.write(filetext)
            self.current_path = pathname[0]
            self.setWindowTitle(pathname[0])

        except Exception as e:
            print(e)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 Text Editor', 'Text files (*.txt)')
        self.setWindowTitle(fname[0])
        with open(fname[0], 'r') as f:
            filetext = f.read()
            self.textEdit.setText(filetext)
        self.current_path = fname[0]

    def save_as_pdf(self):

        fn,_ = QFileDialog.getSaveFileName(self, 'Save file', None,'PDF files(.pdf);;All Files')
        if fn !='' :
            if QFileInfo(fn).suffix()=="" :
                fn+=".pdf"

            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

    def color(self):
        color_ = QColorDialog.getColor(Qt.white,self,"choose color ")
        if color_ :
            self.textEdit.setTextColor(color_)

    def font_(self):

        (self.ok, font) = QFontDialog.getFont()
        print(self.ok)
        if font:
            self.textEdit.setCurrentFont(self.ok)
            print("hello world")

    def python(self):

            self.highlighter = syntax_python.PythonHighlighter(self.textEdit.document())

    def cpp(self):

            self.highlighter = syntax_cpp.Highlighter(self.textEdit.document())


    def defaut(self):

        # self.ok = False
        self.highlighter = self.textEdit.document()

    def addimage(self):
        #Add the image
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 Text Editor',
                                                'Image files (*.png)')

            cursor = QTextCursor(self.textEdit.document());
            p1 = cursor.position()

            cursor.insertImage(fname[0])


        except Exception as e:
            print(e)


    def create_toolbar(self):
        undo_action = QAction(QIcon('src/Resources/icons8-undo-96.png'), 'Undo', self)
        undo_action.triggered.connect(self.textEdit.undo)
        self.toolBar.addAction(undo_action)

        redo_action = QAction(QIcon('src/Resources/icons8-redo-96.png'), 'Redo', self)
        redo_action.triggered.connect(self.textEdit.redo)
        self.toolBar.addAction(redo_action)


        self.toolBar.addSeparator()
        # self.toolBar.addSeparator()

        cut_action = QAction(QIcon('src/Resources/icons8-cut-80.png'), 'Cut', self)
        cut_action.triggered.connect(self.textEdit.cut)
        self.toolBar.addAction(cut_action)

        copy_action = QAction(QIcon('src/Resources/icons8-copy-64.png'), 'Copy', self)
        copy_action.triggered.connect(self.textEdit.copy)
        self.toolBar.addAction(copy_action)

        paste_action = QAction(QIcon('src/Resources/icons8-paste-80.png'), 'Paste', self)
        paste_action.triggered.connect(self.textEdit.paste)
        self.toolBar.addAction(paste_action)

        self.toolBar.addSeparator()
        self.toolBar.addSeparator()

        font_combo = QFontComboBox()
        font_combo.currentFontChanged.connect(self.textEdit.setCurrentFont)
        self.toolBar.addWidget(font_combo)

        font_size_box = QSpinBox()
        font_size_box.setValue(20)
        font_size_box.valueChanged.connect(self.textEdit.setFontPointSize)
        self.toolBar.addWidget(font_size_box)

        self.toolBar.addSeparator()
        # self.toolBar.addSeparator()

        bold_action = QAction(QIcon("src/Resources/icons8-bold-96.png"), 'Bold', self)
        bold_action.triggered.connect(self.bold_text)
        self.toolBar.addAction(bold_action)

        # underline
        underline_action = QAction(QIcon("src/Resources/icons8-underline-80.png"), 'Underline', self)
        underline_action.triggered.connect(self.underline_text)
        self.toolBar.addAction(underline_action)

        # italic
        italic_action = QAction(QIcon("src/Resources/icons8-italic-80.png"), 'Italic', self)
        italic_action.triggered.connect(self.italic_text)
        self.toolBar.addAction(italic_action)


        # separator
        self.toolBar.addSeparator()

        # text alignment

        left_alignment_action = QAction(QIcon("src/Resources/icons8-align-left-96.png"), 'Align Left', self)
        left_alignment_action.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignLeft))
        self.toolBar.addAction(left_alignment_action)

        justification_action = QAction(QIcon("src/Resources/icons8-align-justify-96.png"), 'Center/Justify', self)
        justification_action.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignCenter))
        self.toolBar.addAction(justification_action)


        right_alignment_action = QAction(QIcon("src/Resources/icons8-align-right-96.png"), 'Align Right', self)
        right_alignment_action.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignRight))
        self.toolBar.addAction(right_alignment_action)

        # separator
        # self.toolBar.addSeparator()


        # separator
        self.toolBar.addSeparator()

        dark_action = QAction(QIcon('src/Resources/icons8-moon-96.png'), 'darkmode', self)
        dark_action.triggered.connect(self.dark_mode)
        self.toolBar.addAction(dark_action)

        light_action = QAction(QIcon('src/Resources/sun-9658.png'), 'lightmode', self)
        light_action.triggered.connect(self.light_mode)
        # light_action.
        self.toolBar.addAction(light_action)
        self.toolBar.setIconSize(QtCore.QSize(25, 25))



        # self.setStyleSheet('''
        #                     QToolBar::item:selected{
        #                     background-color: #000000
        #                     }
        #                      ''')


    def OpenPressed(self):
        print("Open Has Been Pressed")

    def set_font_size(self):
        value = self.font_size_box.value()
        self.textEdit.setFontPointSize(value)

    def italic_text(self):
        # if already italic, change into normal, else italic
        state = self.textEdit.fontItalic()
        self.textEdit.setFontItalic(not(state))

    def underline_text(self):
        # if already underlined, change into normal, else underlined
        state = self.textEdit.fontUnderline()
        self.textEdit.setFontUnderline(not(state))

    def dark_mode(self):
        self.setStyleSheet('''QWidget{
                    background-color: rgb(33,33,33);
                    color: #FFFFFF;
                    }
                    QTextEdit{
                    background-color: rgb(46,46,46) !important;
                    }
                    QMenuBar::item:selected{
                    color: #000000
                    }
                     ''')


    def light_mode(self):
        self.setStyleSheet('''
                     ''')
    def bold_text(self):
        # if already bold, make normal, else make bold
        if self.textEdit.fontWeight() != QFont.Bold:
            self.textEdit.setFontWeight(QFont.Bold)
            return
        self.textEdit.setFontWeight(QFont.Normal)
