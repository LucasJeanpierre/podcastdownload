from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

from DownloadFunctions import *

class InitWindow(QMainWindow):
    def __init__(self, file_list, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.setWindowTitle("Python ")
        self.setGeometry(0, 0, self.width, self.height)

        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for element_id in range(len(file_list)):
            button = self.UiComponents(file_list[element_id][0], file_list[element_id][1], element_id)
            self.vbox.addWidget(button)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()
        
       

    def UiComponents(self, title, url, id):
  
        # creating a push button
        button = QPushButton(title, self)
  
        # setting geometry of button
        button.setGeometry(0, 30*id, self.width, 30)
  
        # adding action to a button
        button.clicked.connect(lambda id=id: self.clickme(title, url))

        return button
  
    # action method
    def clickme(self, title, url):
        download_posdact(title, url)
