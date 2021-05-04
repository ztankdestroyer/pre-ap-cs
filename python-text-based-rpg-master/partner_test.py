##car class program
##Zeke and Faizaan
##3/5/21

class Car(object):

    def __init__(self, make, color, gas):
        ##zeke
        self.color = color
        self.make = make
        self.__gas = gas
    
    @staticmethod
    def fuel_guage(self, color, make, gas):
        ##faizaan, tells how much fuel is left
        print("The " + self.color + " " +  self.make + " has used " + gallons_used + " gallons.")

    def __str__():
        ##zeke
        fuel = "The "+ self.color + " " +  self.make + " has " + self.gas + " gallons of fuel." 

    def Drive_around_block(self, gas):
        ##zeke, drives the car around the block and uses 1 gallon of fuel  
        print("The {self.color} {self.make} is driving around the block.")
        gallons_used += 1

    def __refuel(self, gas):
        ##faizaan, if the car runs out of fuel, you have to refuel it
        print("The "+ self.color + " "+ self.make + "is refueling...")
        self.gas = 16

    @property
    def gas():
        return self.__gas
    
    def fill_up():
        self.__refuel() 
    

#main
gallons_used = 0
Car1 = Car("Truck", "Blue", 20)
Car2 = Car("Suburban", "Red", 20)
Car3 = Car("Sedan", "Orange", 15)

print("\t\tWelcome to the Car Simulator!")

Car1.fuel_guage(15)


    
