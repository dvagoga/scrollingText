from tkinter import *
import time

firstWindowLength = 5
middleWindowLength = 1
lastWindowLength = 20

gl = ['у', 'е', 'э', 'о', 'а', 'ы', 'я', 'и', 'ю', 'У', 'Е', 'Э', 'О', 'А', 'Ы', 'Я', 'И', 'Ю']

class console:
    sign = []
    delayTimeIndex = 0
    delayTimeValue = [1000, 500, 400, 300, 200, 175, 150, 125, 100]
    def reduceSpeed(self):
        if self.delayTimeIndex > 0:
            self.delayTimeIndex -= 1
    def increaseSpeed(self):
        if self.delayTimeIndex < (len(self.delayTimeValue)-1):
            self.delayTimeIndex += 1
    def delayTime(self):
        return self.delayTimeValue[self.delayTimeIndex]
    def outputWord(self, wordToDisplay, charColors):
        wordLength = len(wordToDisplay)
        for i in range(len(self.sign)):
            self.sign[i].destroy()
        self.sign = [Label(font='courier 20 bold', borderwidth = 0, width = 1, fg = charColors[i], text = wordToDisplay[i]) for i in range(wordLength)]
        for i in range(wordLength):
            self.sign[i].pack(side = 'left')

class state:
    indexWord = 0
    mode = 'stp'
    def nextWord(self):
        self.indexWord += 1
    def previousWord(self):
        if self.indexWord > 0:
            self.indexWord -= 1
    def setMode(self, event):
        if self.mode == 'stp':
            self.mode = 'go'
            f.after(1, reading)
        else:
            self.mode = 'stp'
    def getMode(self):
        return self.mode

reedText = console()
readControl = state()
allWords = []
targetFile = open('testText.txt', 'r')
fileLines = targetFile.readlines()
targetFile.close()
for line in fileLines:
    words = line.split()
    for word in words:
        allWords.append(word)
root=Tk()

def speedControl(event):
    d = event.delta
    if readControl.getMode() == 'stp':
        if d < 0:
            readControl.nextWord()
            f.after(1, reading)
        else:
            readControl.previousWord()
            f.after(1, reading)
    else:
        if d < 0:
            reedText.increaseSpeed()
        else:
            reedText.reduceSpeed()

def reading():    
    global allWords
    word = allWords[readControl.indexWord]
    wordLength = len(word)
    colors = ['black' for i in range(wordLength)]
    colors[0] = 'red'
    if wordLength > 2:
        colors[wordLength-1] = 'red'
    if wordLength > 6:
        colors[1] = 'red'
        colors[wordLength-2] = 'red'
        colors[wordLength-1] = 'red'
    reedText.outputWord(word, colors)
    if readControl.getMode() != 'stp':
        readControl.nextWord()
        f.after(reedText.delayTime(), reading)

reedText.outputWord('stopped', ['red', 'red', 'red', 'red', 'red', 'red', 'red',])
f = Frame(root, width=100, heigh=100, bg='green', bd=5)
f.after_idle(reading)
root.bind("<MouseWheel>", speedControl)
root.bind("<ButtonPress-1>", readControl.setMode)
root.mainloop()
