from tkinter import *

class SportsBall:
    
    position = 0
    speed = 0
    angle = 0
    meter = 0
    increase = True

    def __init__(self):
        self.position = 0
        self.speed = 0
        self.angle = 0
        self.meter = 0
        self.increase = True

    def changePosition(self):
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
        print(self.meter)

    def changeSpeed(self):
        if self.increase:
            if self.meter < 100:
                self.meter += 10
            else:
                self.increase = False
        else:
            if self.meter > 0:
                self.meter -= 10
            else:
                self.increase = True

    def changeAngle(self):
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

master = Tk()

w = Canvas(master, width=400, height=600)
w.pack()

w.create_rectangle(100, 575, 300, 25, fill="#d3d34d")
w.create_rectangle(50, 575, 100, 25, fill="#2b3030")
w.create_rectangle(300, 575, 350, 25, fill="#2b3030")
w.create_oval(175, 575, 225, 525, fill="red")

mainloop()