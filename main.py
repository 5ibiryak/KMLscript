from cmath import pi

import os
from os import listdir

import sys
from PyQt5 import QtWidgets
from style import *
from PyQt5.QtWidgets import QMessageBox
from bs4 import BeautifulSoup
import re

path_folders=''
def getFolder():
    global path_folders
    path_folders = QtWidgets.QFileDialog.getExistingDirectory()
    ui.plainTextEdit_folder.setPlainText(format(path_folders))

world=[]
def move():
    try:
        print(path_folders)
        os.chdir(path_folders)
    except:
        pass
    try:
        for i in range(3,1000):
            if i<10:
                print('DSC0000'+ str(i) +'.kml')
                file_name='DSC0000'+ str(i) +'.kml'
            elif(i<100):
                print('DSC000'+ str(i) +'.kml')
                file_name='DSC000'+ str(i) +'.kml'
            elif(i>=100):
                print('DSC00'+ str(i) +'.kml')
                file_name='DSC00'+ str(i) +'.kml'

            with open(file_name, 'r') as f:
                s = BeautifulSoup(f, 'xml')
                name = re.search(r"(\w{8}).JPG",str(s))
                altitude = re.search(r"([^<>]{8,9})</geogr:RelativeAltitude>",str(s))
                elevation = re.search(r"([^<>]{8,9})</geogr:Elevation>",str(s))
                pitch = re.search(r"<kml:pitch>(\S{7,10})</kml:pitch>",str(s))
                roll = re.search(r"<kml:roll>(\S{7,10})</kml:roll>",str(s))
                yaw = re.search(r"<kml:yaw>(\S{7,10})</kml:yaw>",str(s))
                latitude = re.search(r"<kml:latitude>(\S{7,10})</kml:latitude>",str(s))
                longtitude = re.search(r"<kml:longitude>(\S{7,10})</kml:longitude>",str(s))
                # print(name[0])
                # print(altitude[1])
                # print(elevation[1])
                # print(pitch[1])
                # print(roll[1])
                # print(yaw[1])
                # print(latitude[1])
                # print(longtitude[1])
                all=f"{name[0]},{altitude[1]},{elevation[1]},{pitch[1]},{roll[1]},{yaw[1]},{latitude[1]},{longtitude[1]}\n"
                with open('out.txt', 'w') as file:
                    world.append(all)
                    file.writelines(world)
    except:
        pass

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()



ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.pushButton_folder.clicked.connect(getFolder)
ui.pushButton.clicked.connect(move)

sys.exit(app.exec_())
