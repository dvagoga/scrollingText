from tkinter import *


import time
def tick():
    label.after(200, tick)
    label['text'] = time.strftime('%H:%M:%S')    
root=Tk()
label = Label(font='sans 20')
label.pack()
label.after_idle(tick)
root.mainloop()


class st:
    s = 1
    tt = []
    t = 20
    def setS(self, v):
        self.s = 0
        fl = open('testText.txt', 'r')
        t = fl.readlines()
        fl.close()
        for ln in t:
            wrd = ln.split()
            for w in wrd:
                self.tt.append(w)
    def getS(self):
        return self.tt[self.s]#, self.tt[self.s+1], self.tt[self.s+2]
    def incS(self):
        self.s += 1
    def decS(self):
        if self.s != 1:
            self.s -= 1
    def incT(self):
        if self.t < 100:
            self.t += 1
        else:
            self.decS()
    def decT(self):
        if self.t > 10:
            self.t -= 1
ss = st()
ss.setS(0)
print('start')
root=Tk()

def ctrl(event):
    d = event.delta
    if d < 0:
        ss.decT()
    else:
        ss.incT()

def scrl():
    l.after(ss.t*20, scrl)
    ss.incS()
    l['text'] = ss.getS()
    print(ss.getS())

l = Label(font='sans 20')
l.pack()
label.after_idle(scrl)
root.bind("<MouseWheel>", ctrl)
root.mainloop()
