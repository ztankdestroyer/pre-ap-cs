from tkinter import *
 
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self["background"] = "#4d4d4d"
        self.create_widgets()
 
    def create_widgets(self):
        Label(self,
              text = "Enter information for a new story", bg = "#4d4d4d", fg = "#AFEADC", font=("Times New Roman", 18, "bold")
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
 
        Label(self,
              text = "Person: ", bg = "#4d4d4d", fg = "#AFEADC", font=("Times New Roman", 11, "bold")
              ).grid(row = 1, column = 0, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)
        self.person_ent["background"] = "#AFEADC"
        self.person_ent["borderwidth"] = 0
 
        Label(self,
              text = "Plural Noun:", bg = "#4d4d4d", fg = "#AFEADC", font=("Times New Roman", 11, "bold")
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)
        self.noun_ent["background"] = "#AFEADC"
        self.noun_ent["borderwidth"] = 0

        Label(self,
              text = "Verb:", bg = "#4d4d4d", fg = "#AFEADC", font=("Times New Roman", 11, "bold")
              ).grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)
        self.verb_ent["background"] = "#AFEADC"
        self.verb_ent["borderwidth"] = 0
     
        Label(self,
              text = "Adjective(s):", bg = "#4d4d4d", bd = 0, fg = "#AFEADC", font=("Times New Roman", 11, "bold")
              ).grid(row = 4, column = 0, sticky = W)
 
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "poggers", bg = "#4d4d4d", bd = 0, fg = "#AFEADC", font=("Times New Roman", 11, "bold"),
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)
 
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "exausted", bg = "#4d4d4d", bd = 0, fg = "#AFEADC", font=("Times New Roman", 11, "bold"),
                    variable = self.is_joyous
                    ).grid(row = 4, column = 2, sticky = W)
 
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "horified", bg = "#4d4d4d", bd = 0, fg = "#AFEADC", font=("Times New Roman", 11, "bold"),
                    variable = self.is_electric
                    ).grid(row = 4, column = 3, sticky = W)
 
        Label(self,
              text = "Body Part:", bg = "#4d4d4d", bd = 0, fg = "#AFEADC", font=("Times New Roman", 11, "bold")
              ).grid(row = 5, column = 0, sticky = W)
 
        self.body_part = StringVar()
        self.body_part.set(None)
  
        body_parts = ["head", "right leg", "right middle finger"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part, bg = "#4d4d4d", bd = 0, fg = "#AFEADC", font=("Times New Roman", 11, "bold"),
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1
 
        Button(self,
               text = "Click for story", bg = "#4d4d4d", bd = 0, fg = "#AFEADC", font=("Times New Roman", 11, "bold"),
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
 
        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD, fg = "#AFEADC", bg = "#4d4d4d", bd = 0, font=("Times New Roman", 11, "bold"))
        self.story_txt.grid(row = 7, column = 0, columnspan = 4)
 
    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "Poggers, "
        if self.is_joyous.get():
            adjectives += "exausted, "
        if self.is_electric.get():
            adjectives += "horified, "
        body_part = self.body_part.get()
 
        story = "While trying to clean his boat "
        story += person
        story += " was using a mop to clean his "
        story += noun.title()
        story += " when one day, the "
        story += noun
        story += " found "
        story += person + " sitting on a stump."
        story += "A strong, "
        story += adjectives
        story += "peculiar feeling overwhelmed " + person + "."
        story += "After all this time, the boat was finally clean. A tear came to "
        story += person + "'s "
        story += body_part + ". "
        story += "And then, the "
        story += noun
        story += " randomly devoured "
        story += person + ". "
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."
                                     
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)
 
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()
