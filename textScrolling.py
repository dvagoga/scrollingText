from tkinter import *
import time

gl = ['у', 'е', 'э', 'о', 'а', 'ы', 'я', 'и', 'ю']

class st:
    currentWord = 0
    allWords = []
    delayTimeIndex = 0
    #delayTimeValue = [2000, 1000, 500, 250, 125, 62, 31, 15, 7]
    delayTimeValue = [2000, 500, 400, 300, 200, 175, 150, 125, 100]
    def init(self):
        self.currentWord = 0
        self.delayTimeIndex = 0
        targetFile = open('testText.txt', 'r')
        fileLines = targetFile.readlines()
        targetFile.close()
        for line in fileLines:
            words = line.split()
            for word in words:
                self.allWords.append(word)
    def getWord(self):
        if self.currentWord < len(self.allWords):
            self.currentWord += 1
        return self.allWords[self.currentWord]#, self.tt[self.s+1], self.tt[self.s+2]
    def stopSpeed(self):
        self.delayTimeIndex = 0
    def reduceSpeed(self):
        if self.delayTimeIndex > 0:
            self.delayTimeIndex -= 1
        else:
            if self.currentWord != 1:
                self.currentWord -= 1
    def increaseSpeed(self):
        if self.delayTimeIndex < (len(self.delayTimeValue)-1):
            self.delayTimeIndex += 1
    def delayTime(self):
        return self.delayTimeValue[self.delayTimeIndex]

ss = st()
ss.init()
root=Tk()

def speedControl(event):
    d = event.delta
    if d < 0:
        ss.increaseSpeed()
    else:
        ss.reduceSpeed()

def reading():    
    word = "  " + ss.getWord()
    spaceNum = 0
    if len(word) % 2 == 0:
        spaceNum = len(word)//2
    else:
        spaceNum = (len(word)+1)//2

    #check = False
    #while not check:
    #    if word[spaceNum] in gl:
    #        check = True
    #    else:
    #        if spaceNum == (len(word) - 1):
    #            check = True
    #        else:
    #            spaceNum += 1

    l['text'] = word[:spaceNum]
    l2['text'] = word[spaceNum]
    l3['text'] = word[spaceNum+1:]
    l.after(ss.delayTime(), reading)



def stp(event):
    ss.stopSpeed()

l = Label(font='courier 20 bold', borderwidth = 0, width = 10, anchor= E)
l.pack(side = 'left')
l2 = Label(font='courier 20 bold', borderwidth = 0,  width = 1, fg = 'red', bg = 'gray')
l2.pack(side = 'left')
l3 = Label(font='courier 20 bold', borderwidth = 0, width = 15, anchor= W,)
l3.pack(side = 'left')
l.after_idle(reading)
root.bind("<MouseWheel>", speedControl)
root.bind("<ButtonPress-1>", stp)
root.mainloop()
