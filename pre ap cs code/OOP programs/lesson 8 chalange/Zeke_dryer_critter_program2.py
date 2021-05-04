import random
feed_ammount = 1
play_ammount = 1
unhappiness = 0
class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def __str__(self):
        return ("Hunger: {self.hunger} \nBoredom: {self.boredom} \nunhappiness: {unhappiness}")

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1


    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Exhilarated"
        elif 5 <= unhappiness <= 10:
            m = "Mediocre"
        elif 11 <= unhappiness <= 15:
            m = "Livid"
        else:
            m = "Furious"
        return m
    
    def stats(self):
        print(self.name)
        print("unhappiness: " , unhappiness)
        print("hunger: " , self.hunger)
        print("boredom: " , self.boredom)
        print("\n")
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self, food = (feed_ammount * 4)):
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = (play_ammount * 4)):
        print("says Wheee!")
        self.boredom -= fun 
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name1 = input("What do you want to name your first critter?: ")
    crit1 = Critter(crit_name1, random.randrange(0 , 3 , 1), random.randrange(0 , 5 , 1))

    crit_name2 = input("What do you want to name your second critter?: ")
    crit2 = Critter(crit_name2, random.randrange(0 , 3 , 1), random.randrange(0 , 5 , 1))

    crit_name3 = input("What do you want to name your third critter?: ")
    crit3 = Critter(crit_name3, random.randrange(0 , 3 , 1), random.randrange(0 , 5 , 1))

    crit_name4 = input("What do you want to name your forth critter?: ")
    crit4 = Critter(crit_name4, random.randrange(0 , 3 , 1), random.randrange(0 , 5 , 1))

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Good-bye.")

        elif choice == "1":
            crit1.talk()
            crit2.talk()
            crit3.talk()
            crit4.talk()
        
        elif choice == "2":
            feed_ammount = input("how many times would you like to feed it? ")    
            crit1.eat()
            crit2.eat()
            crit3.eat()
            crit4.eat()
            
        elif choice == "3":
            play_ammount = input("how many times do you want to play with it? ")
            crit1.play()
            crit2.play()
            crit3.play()
            crit4.play()

        elif choice == "secret":
            crit1.stats()
            crit2.stats()
            crit3.stats()
            crit4.stats()
            
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
