
from User import User
from SysCallManager import SysCallManager


class RegistryAgent(User):
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
        # show possible services for Registry Agent
        accessServices = True
        while (accessServices):
            self.showGreeting()
            print("###### Registry Agent Services Dashboard ######")
            print("Enter (1) to register a birth")
            print("Enter (2) to register a marriage")
            print("Enter (3) to renew vehicle registration")
            print("Enter (4) to process a bill of sale")
            print("Enter (5) to process a payment")
            print("Enter (6) to get a driver's abstract")
            print("Enter (7) to exit and log out of the session\n")
            response = input("please enter an action: ")
            print("\n")
            if (response == "1"):
                self.registerBirth()
            elif (response == "2"):
                self.registerMarriage()
            elif (response == "3"):
                self.renewVehicleRegistration()
            elif (response == "4"):
                self.processBillOfSale()
            elif (response == "5"):
                self.processPayment()
            elif (response == "6"):
                self.getDriverAbstract()
            elif (response == "7"):
                accessServices = False
            else:
                print("the action you selected is not recognized, try again\n")

    def registerBirth(self):
        # allow registry agent to register a birth
        # perform issue ticket steps

        ##################################################################################
        # register birt SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully registered birth\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def registerMarriage(self):
        # allow registry agent to register a marriage
        # perform issue ticket steps
        ##################################################################################
        # register marriage SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully registered marriage\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def renewVehicleRegistration(self):
        # allow registry agent to renew their registration
        # perform issue ticket steps

        ##################################################################################
        # renew vehicle registration SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully renewed vehicle registration\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def processBillOfSale(self):
        # allow rgistry agent to process a bill of sale
        # perform issue ticket steps

        ##################################################################################
        # process bill of sale SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully processed bill of sale\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def processPayment(self):
        # allow registry agent to process a payment
        # perform issue ticket steps

        ##################################################################################
        # process payment SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully processed payment\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def getDriverAbstract(self):
        # allow registry agent to get a driver abstract
        # perform issue ticket steps

        ##################################################################################
        # get driver abstract SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully retrieved driver abstract\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()
        