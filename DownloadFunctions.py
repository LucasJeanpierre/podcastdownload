import requests
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory
import os

def download_posdact(title, file_url):
    global path
    question = askquestion('Download', 'You want to download : ' + title)
    if question == 'yes' :
        print(title, file_url)
        new_title = title.replace(':','').replace(' ', '_').replace('/','_sur_')
        filepath = os.path.join(path, new_title[:240] +'.mp3')
        file = requests.get(file_url)
        with open(filepath, 'wb') as f:
                f.write(file.content)


def get_file_list(content):
    file_list = []
    for item in content['rss']['channel']['item']:
        title = item['title']
        file_url = item['enclosure']['@url']
        #print(title, file_url)
        file_list.append((title, file_url))
    return file_list


def setPath():
    global path
    root = Tk()
    root.withdraw()

    path = askdirectory(title='Select Folder')

def setUrl(new_url):
    global url
    url = new_url