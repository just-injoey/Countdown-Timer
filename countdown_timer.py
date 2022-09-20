from tkinter import *
import tkinter as tk

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.pack()
        self.createWidgets()
        
        self.master.geometry("500x200")
        self._alarm_id = None
        self._paused = False
        self._starttime = 0
    
    # def startTimer(self):

    def createWidgets(self):

        self.someFrame = Frame(self)
        self.time_var = StringVar()
        self.input_time = tk.Entry(self, width=25, font=('Calibri',12), textvariable = self.time_var)
        # Adding placeholder
        self.input_time.insert(0, "Enter Time in seconds")
        self.input_time.pack(padx=10,pady=(30,10))
        #using bind method
        self.input_time.bind("<Button-1>", self.enter)
        
        self.startButton = Button(self.someFrame, text="Start", font=('Helvetica',12), bg='green', fg='white', command=self.startTime)
        self.startButton.pack(side=LEFT, padx=5)

        self.pauseButton = Button(self.someFrame, text="Pause", font=('Helvetica',12), bg='azure', command=self.pauseTime)
        self.pauseButton.pack(side=LEFT, padx=5)

        self.resetButton = Button(self.someFrame, text="Reset", font=('Helvetica',12), bg='azure', command=self.resetTime)
        self.resetButton.pack(side=LEFT, padx=5)

        self.closeButton = Button(self.someFrame, text="Close", font=('Helvetica',12), bg='red',fg='white', command=self.closeApp)
        self.closeButton.pack(side=LEFT, padx=5)
        self.someFrame.pack(side=TOP)

        self.labelvariable = StringVar()
        self.labelvariable.set("")

        self.thelabel = Label(self,textvariable = self.labelvariable,font=('Helvetica',50))
        self.thelabel.pack(side=TOP)

    # Removes placeholder text in the Entry widget
    def enter(self,*args):
        self.input_time.delete(0, 'end')
        
        




if __name__ == '__main__':
    root = Tk()
    root.title("Countdown Timer")
    app = Application(root)
    root.mainloop()
 
