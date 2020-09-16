from tkinter import *
import time
import math

class SportsBall:
    
    position = 0
    angle = 0
    speed = 0
    meter = 0
    increase = True
    state = 0

    def __init__(self):
        self.position = 0
        self.angle = 0
        self.speed = 0
        self.meter = 0
        self.increase = True

        self.root = Tk()
        self.w = Canvas(self.root, width=400, height=600)
        self.w.pack()

        self.w.create_rectangle(100, 575, 300, 25, fill="#d3d34d")
        self.w.create_rectangle(50, 575, 100, 25, fill="#2b3030")
        self.w.create_rectangle(300, 575, 350, 25, fill="#2b3030")
        self.b = self.w.create_oval(175, 575, 225, 525, fill="red")
        self.l = self.w.create_line(200, 550, 200, 525, fill="black")

        def select(event):
            self.state += 1
            self.meter = 0

        self.w.focus_set()
        self.w.bind("<space>", select)
        self.w.pack()
        self.doSomething()
        self.root.mainloop()

    def doSomething(self):
        while True:
            if self.state == 0:
                time.sleep(0.025)
                self.w.update()
            elif self.state == 1:
                time.sleep(0.025)
                c = self.changePosition()
                self.w.move(self.b, c, 0)
                self.w.move(self.l, c, 0)
                self.w.update()
            elif self.state == 2:
                time.sleep(0.025)
                c = self.changeAngle()
                self.w.update()
            elif self.state == 3:
                time.sleep(0.025)
                c = self.changeSpeed()
                self.w.move(self.b, 0, c)
                self.w.move(self.l, 0, c)
                self.w.update()
            elif self.state == 4:
                self.state = 0

    def changePosition(self):
        t = self.meter
        if self.increase:
            if self.meter < 100:
                self.meter += 10
            else:
                self.increase = False
        else:
            if self.meter > -100:
                self.meter -= 10
            else:
                self.increase = True
        return self.meter - t

    def changeAngle(self):
        t = self.meter
        if self.increase:
            if self.meter < 100:
                self.meter += 10
            else:
                self.increase = False
        else:
            if self.meter > -100:
                self.meter -= 10
            else:
                self.increase = True
        return self.meter - t

    def changeSpeed(self):
        t = self.meter
        if self.increase:
            if self.meter < 100:
                self.meter += 10
            else:
                self.increase = False
        else:
            if self.meter > -100:
                self.meter -= 10
            else:
                self.increase = True
        return self.meter - t

SportsBall()