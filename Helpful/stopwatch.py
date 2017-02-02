# Stopwatch

# Import time library
import time

# Import Tkinter library as "tk"
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def quit():
      (self, command=root.destroy)
  
    def create_widgets(self):
        self.start = tk.Button(self)
        self.start["text"] = "Start Stopwatch"
        self.start["command"] = self.startWatch
        self.start.pack(side="top")
        self.end = tk.Button(self)
        self.end["text"] = "Stop Stopwatch"
        self.end["command"] = self.stopWatch
        self.end.pack(side="top")
        

    def startWatch(self):
        # Create three variables: hour, minute, and second. Give them the value of 0.
        hour = 00
        minute = 00
        second = 00

        watchBegin = input('Start stopwatch? Type "yes" or "no". Case-sensitive.')
        if watchBegin == 'yes':
          if second > 60:
            minute = minute + 1
            second = 00

          if second < 60:
            time.sleep(1)
            second = second + 1

          if minute > 60:
            hour = hour + 1
            minute = 00

          print('Type nothing in the field below to continue.')
          watchStop = input('Stop stopwatch? Case-sensitive "yes".')

          if watchBegin == 'yes':
            print('Current time elasped:', hour,':',minute,':',second)
            
     def stopWatch(self):
         

root = tk.Tk()
app = Application(master=root)
app.mainloop()
