
from User import User
from SysCallManager import SysCallManager


class TrafficOfficer(User):
    # inherit from base properties of user
    def __init__(self, uType, name):
        self.userType = uType
        self.fullname = name

    def getUserType(self):
        # super().getUserType()
        return self.userType

    def getUserFullName(self):
        # super().getUserFullName()
        return self.fullname

    def showGreeting(self):
        header = "###################################################################################"
        greeting = " Welcome, " + self.fullname + " "
        middleHeader = ""
        fillerLength = (len(header) - len(greeting)) // 2
        middleHeader += "#"
        for i in range(fillerLength - 1):
            middleHeader += "-"
        middleHeader += greeting
        for i in range(fillerLength - 1):
            middleHeader += "-"
        middleHeader += "#"

        print(header)
        print(middleHeader)
        print(header + "\n")

    def accessUserServices(self):
        SysCallManager.clearWindow()
        # super().accessUserServices()
        # show possible services for a Traffic Officer
        accessServices = True
        while (accessServices):
            self.showGreeting()
            print("###### Traffic Officer Services Dashboard ######")
            print("Enter (1) to issue a ticket")
            print("Enter (2) to find a specific car's owner")
            print("Enter (3) to exit and log out of the session\n")
            response = input("please enter an action: ")
            print("\n")
            if (response == "1"):
                self.issueTicket()
            elif (response == "2"):
                self.findCarOwner()
            elif (response == "3"):
                accessServices = False
            else:
                print("the action you selected is not recognized, try again\n")

    def issueTicket(self):
        # allow the traffic officer to issue ticket
        # perform issue ticket steps

        ##################################################################################
        # issue ticket SQL logic goes here


        # end logic
        ##################################################################################


        print("successfully issued ticket\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def findCarOwner(self):
        # allow the traffic officer to find a car owner
        # perform issue ticket steps

        ##################################################################################
        # issue ticket SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully found car owner\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

        