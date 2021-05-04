from tkinter import *
import random
 
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
        self["background"] = "pink"
        self["borderwidth"] = 0

    def newnum(self):
        global i 
        i = random.randint(1,125)
 
    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Guess a random number between 1 and 125", bg = "pink")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
    
        self.pw_lbl = Label(self, text = "Guessed number: ", bg = "pink")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
     
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        self.pw_ent["background"] = "#F8C8DC"

        self.newnum_bttn = Button(self, text = "New Num", bg = "pink",command = self.newnum)
        self.newnum_bttn.grid(row = 2, column = 0, sticky = W)
 
        self.submit_bttn = Button(self, text = "Submit", bg = "pink", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 1, sticky = W)

        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)
        self.secret_txt["background"] = "pink"
        self.secret_txt["borderwidth"] = 0
 
    def reveal(self):
        contents = float(self.pw_ent.get())

        if contents == i:
            message = "Congrats You Got it"     
        elif contents > i:
            message = "sorry your number is too high"    
        elif contents < i:
            message = "sorry your number is too low "
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)
 
root = Tk()
root.title("Nummber Guesser")
root.geometry("300x150")
 
app = Application(root)
 
root.mainloop()
