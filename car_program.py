class Car(object):
    def __init__(self, Make, Color ,gas = 20):
        self.Make = Make
        self.Color = Color
        self.gas = gas

    def __Driven(self):
        self.gas -= 1


    def Refuel(self,  fuel= 20):
        self.gas += fuel
        if self.gas >= 20:
            self.gas = 20
        print("Your tank is now full and you have 20 gallons of gas")

    def Drive(self, used = 2):
        self.gas -= used
        self.__Driven()
        if self.gas <= 0:
          self.gas = 0
          print("Your Out of gas!")
        print("You now have " + str(self.gas) + " gallons of gas")
def main():
    car_make = input("What is the model of your car?: ")
    car_color = input("What is the color of your car?: ")
    Car1 = Car(car_make, car_color)

    choice = None
    while choice != "0":
        print \
        ("""
        Car Simulator
    
        0 - Quit
        1 - Drive your car
        2 - Refuel your car
        """)
    
        choice = input("Choice: ")
        print()

        if choice == "0":
            print("THanks for playing.")

        elif choice == "1":
            Car1.Drive()
        
        elif choice == "2":
            Car1.Refuel()

        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
