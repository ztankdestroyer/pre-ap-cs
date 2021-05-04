class TV(object):
    def __init__(self, name, volume = 0, channel = 1):
        self.name = name
        self.volume = volume
        self.channel = channel

    def channel_ups(self):
        self.channel += 1
        if (self.channel +1) == 21:
            self.channel = 1
        

    def channel_downs(self):
        self.channel -= 1
        if (self.channel -1) == 0:
            self.channel = 20
            

    def volume_ups(self):
        self.volume += 1
        if (self.volume +1) == 51:
            self.volume = 1

    def volume_downs(self):
        self.volume -= 1
        if (self.volume -1) == -1:
            self.volume = 0
            print("the volume Cannot go below 0!")


    def stats(self):
        print("volume: " , str(self.volume))
        print("channel: " , str(self.channel))
    
    def volume_up(self):
        self.volume_ups()
        print("your new volume is: " + str(self.volume))
    
    def volume_down(self):
        self.volume_downs()
        print("your new volume is: " + str(self.volume))

    def channel_up(self):
        self.channel_ups()
        print("your new channel is: " + str(self.channel))
    
    def channel_down(self):
        self.channel_downs()
        print("your new channel is: " + str(self.channel))

def main():
    naming = input("Would you like to give your tv a nickname? ")
    if naming == "yes":
        tv_name = input("What nickname do you want to give your tv?: ")
        tv = TV(tv_name)
    else:
        tv_name = ("TV")
        tv = TV(tv_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        TV options
    
        0 - Quit
        1 - Volume up
        2 - Volume down
        3 - Channel down
        4 - Channel up
        5 - Check Volume and Channel
        """)
    
        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Good-bye.")

        elif choice == "1":
            tv.volume_up()
        
        elif choice == "2":
            tv.volume_down()
            
        elif choice == "3":
            tv.channel_down()

        elif choice == "4":
            tv.channel_up()

        elif choice == "5":
            tv.stats()
        
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()

