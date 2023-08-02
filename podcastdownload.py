import requests
import xmltodict
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import os
from MainWindow import MainWindow
import sys


from MainWindow import MainWindow
from DownloadFunctions import *

    
#create exe with pyinstaller
#pyinstaller --onefile --windowed --icon=icon.ico podcastdownload.py

def createMainWindow(file_list):

    width = 800
    height = 800

    App = QApplication(sys.argv)
    window = MainWindow(file_list, width, height)
    sys.exit(App.exec())



def validateInit(url, root):
    root.destroy()
    global response
    setUrl(url)

    response = requests.get(url).text
    content = xmltodict.parse(response)
    file_list = get_file_list(content)
    createMainWindow(file_list)


def inputWindow():
    root = Tk()
    root.geometry("400x400")
    root.title("Podcast Downloader")
    root.iconbitmap('icon.ico')
    label = Label(root, text="URL : ")
    input = Entry(root)
    button_url = Button(root, text="Validate", command= lambda:validateInit(input.get(), root))
    button_path = Button(root, text="Select path", command= lambda:setPath())

    label.pack()
    input.pack()
    button_path.pack()
    button_url.pack()


    root.mainloop()


inputWindow()
