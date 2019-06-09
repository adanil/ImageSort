from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import glob, os
import shutil



rowPosition = 3
keys = []
saveDir = []
images = []
currentFile = 0
keySaveDir = {}

def openDirectory(event):
    directoryName = fd.askdirectory()
    dir.insert(0,directoryName)



def accepted(event):
    global dirName
    dirName = dir.get()
    os.chdir(dirName)
    for file in glob.glob("*.png"):
        images.append(file)
    for file in glob.glob("*.jpg"):
        images.append(file)

def addKeyWidget(event):
    global rowPosition
    keyLabel = Label(root,width=5)
    keyLabel['text'] = 'Key:'
    key = Entry(root,width=3)
    keys.append(key)
    DirectLabel = Label(root,width=10)
    DirectLabel['text'] = 'Directory:'

    directToSave = Entry(root,width=20)
    saveDir.append(directToSave)
    keyLabel.grid(row=rowPosition,column=0,sticky=E)
    key.grid(row=rowPosition, column=1,sticky=W)
    DirectLabel.grid(row=rowPosition,column=2,sticky=E)
    directToSave.grid(row=rowPosition,column=3,sticky=E)

    rowPosition += 1

def start(event):
    global keySaveDir
    print('hi')
    for i in range(len(keys)):
        keySaveDir.update({keys[i].get():saveDir[i].get()})
    global imgCanvas
    imgCanvas = Canvas(root, width=700, height=700,bg='white')
    imgCanvas.grid(row=rowPosition, column=0, columnspan=3, rowspan=2)
    pilImage = Image.open(dirName + '/' + images[0])
    image = ImageTk.PhotoImage(pilImage)
    imgCanvas.create_image(400, 400, image=image,anchor=CENTER)
    imgCanvas.image = image
    root.bind('<Key>', save)


def save(event):
    global currentFile
    print('I have successfully waited until %s keypress!' % event.keysym)
    if (currentFile < len(images)):
        if (str(event.keysym) in keySaveDir.keys()):
            global kCanvas
            savePath = keySaveDir[str(event.keysym)]
            #print(savePath)
            shutil.move(dirName + '/' + images[currentFile], savePath)
            currentFile += 1
            if (currentFile >= len(images)):
                endLabel = Label(root, width=30, bg='orange')
                endLabel['text'] = 'Images directory is empty!'
                endLabel.grid(row=rowPosition, column=0)
                kCanvas.delete(ALL)
            else:
                kCanvas = Canvas(root, width=800, height=800, bg='white')
                kCanvas.grid(row=rowPosition, column=0, columnspan=3, rowspan=2)
                pilImage = Image.open(dirName + '/' + images[currentFile])
                image = ImageTk.PhotoImage(pilImage)
                kCanvas.create_image(400, 400, image=image, anchor=CENTER)
                kCanvas.image = image
        else:
            print('Key is not available')
    else:
        endLabel = Label(root,width=30,bg = 'orange')
        endLabel['text'] = 'Images directory is empty!'
        endLabel.grid(row=rowPosition,column=0)
    #print('here')


root = Tk()

root.geometry('1200x800')
root.title('ImageSort')
root.rowconfigure(9, {'minsize': 10})

chooseSourceDir = Label(root, bg='orange', fg='white', width=20)
chooseSourceDir['text'] = 'Choose source directory:'

chooseDirButton = Button(root, text="Choose",width=10)
chooseDirButton.bind('<Button-1>', openDirectory)

dir = Entry(root, width=30)

acceptButton = Button(root,text='Accept',width=10)
acceptButton.bind('<Button-1>',accepted)

chooseKeys = Label(root,bg = 'orange',fg='white',width=20)
chooseKeys['text'] = 'Set keys and directories'

addKeyButton = Button(root,text='add key',width=20,height=1)
addKeyButton.bind('<Button-1>',addKeyWidget)

startButton = Button(root,text='Start',width=20,height=1)
startButton.bind('<Button-1>',start)

chooseSourceDir.grid(row=0,column=0)
dir.grid(row=0,column=1,columnspan=2)
chooseDirButton.grid(row=1,column=2)
acceptButton.grid(row=1,column=1)
chooseKeys.grid(row=2,column=0)
addKeyButton.grid(row=2,column=1)
startButton.grid(row=2,column=2)






root.mainloop()