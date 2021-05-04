from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
        self["background"]  = "#55DFF8"

    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Guess a random number between 1 and 25", bg = "#ADEBF7", font = "script")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
    
        self.pw_lbl = Label(self, text = "Guessed number: ", bg = "#ADEBF7", font = "script")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)
     
        self.pw_ent = Entry(self, bg = "#ADEBF7", font = "New-Bost")
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        self.submit_bttn = Button(self, text = "Submit", bg = "#ADEBF7", font = "script", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt["background"] = "#55DFF8"
        self.secret_txt["font"] = "script"
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def reveal(self):
        contents = self.pw_ent.get()
        i = random.randint(1,25)
        if contents == i:
            message = "Congrats You Got it"         
        else:
            message = "That's not the correct Number " \
                      "Sorry."
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

root = Tk()
root.title("Number Guesser")
root.geometry("300x150")

app = Application(root)

root.mainloop()