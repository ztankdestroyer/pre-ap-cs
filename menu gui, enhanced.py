from tkinter import *
 
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
        self["background"] = "#ADEBF7"
        self["borderwidth"] = 0
 
    def create_widgets(self):
        Label(self,
              text = "Restaurant menu", bg = "#ADEBF7", bd = 0
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
 
 
     
        Label(self,
              text = "Meals(s):", bg = "#ADEBF7", bd = 0
              ).grid(row = 4, column = 0, sticky = W)
 
        self.is_Burger = BooleanVar()
        Checkbutton(self,
                    text = "Burger", bg = "#ADEBF7", bd = 0,
                    variable = self.is_Burger
                    ).grid(row = 4, column = 1, sticky = W)
 
        self.is_Dump = BooleanVar()
        Checkbutton(self,
                    text = "Chicken And Dumplins", bg = "#ADEBF7", bd = 0,
                    variable = self.is_Dump
                    ).grid(row = 4, column = 2, sticky = W)
 
        self.is_chick = BooleanVar()
        Checkbutton(self,
                    text = "Fried Chicken", bg = "#ADEBF7", bd = 0,
                    variable = self.is_chick
                    ).grid(row = 4, column = 3, sticky = W)
 
        Label(self,
              text = "Drinks:", bg = "#ADEBF7", bd = 0
              ).grid(row = 5, column = 0, sticky = W)
 
        self.Drink = StringVar()
        self.Drink.set(None)
  
        Drink = ["Water", "Juice", "Soda"]
        column = 1
        for part in Drink:
            Radiobutton(self,
                        text = part, bg = "#ADEBF7", bd = 0,
                        variable = self.Drink,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        Label(self,
            text = "Tips:", bg = "#ADEBF7", bd = 0
            ).grid(row = 6, column = 0, sticky = W)
 
        self.Tips = StringVar()
        self.Tips.set(None)
  
        Tips = ["5%", "10%", "15%"]
        column = 1
        for part in Tips:
            Radiobutton(self,
                        text = part, bg = "#ADEBF7", bd = 0,
                        variable = self.Tips,
                        value = part
                        ).grid(row = 6, column = column, sticky = W)
            column += 1
 
        Button(self,
               text = "Click for total", bg = "#ADEBF7", bd = 0,
               command = self.show_menu
               ).grid(row = 7, column = 0, sticky = W)
 
        self.final_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.final_txt.grid(row = 8, column = 0, columnspan = 4)
 
    def show_menu(self):
        price = 0
        cost = 0
        tip = 0
        rounded_tip = 0
        if self.is_Burger.get():
            price += 12.99
        if self.is_Dump.get():
            price += 15.99
        if self.is_chick.get():
            price += 9.99
        current_Drink = self.Drink.get()
 
        if current_Drink == "Water":
            cost += 1.99
        if current_Drink == "Juice":
            cost += 3.99
        if current_Drink == "Soda":
            cost += 3.99

        current_Tip = self.Tips.get()

        if current_Tip == "5%":
            tip = ((price + cost) * .05)
            rounded_tip = round(tip, 2)
        if current_Tip == "10%":
            tip = ((price + cost) * .1)
            rounded_tip = round(tip, 2)
        if current_Tip == "15%":
            tip = ((price + cost) * .15)
            rounded_tip = round(tip, 2)

        final = "$"
        final +=str(price + cost + rounded_tip)
        
        self.final_txt.delete(0.0, END)
        self.final_txt.insert(0.0, final)
        self.final_txt["background"] = "#ADEBF7"
        self.final_txt["borderwidth"] = 0
root = Tk()
root.title("Menu")
app = Application(root)
root.mainloop()
