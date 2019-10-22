
from User import User
from SysCallManager import SysCallManager
from cursor import sqlCursor
from InputFormatter import InputFormatter


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

        cursor = sqlCursor.get_instance().get_cursor()
        regno = input("enter registration number: ")
        ##################################################################################
        # issue ticket SQL logic goes here
        cursorResponse = cursor.execute(
            "Select r.fname, r.lname, v.make, v.model, v.year, v.color " \
            "From tickets As t, registrations As r, vehicles As v" \
            "Where t.regno = r.regno And r.vin = v.vin"
        )
        print(cursorResponse)

        response = InputFormatter.ensureValidInput("proceed to issue ticket? (Y/N)", "y", "Y", "n", "N")
        if (response.upper() == "Y"):
            violationDate = input("enter violation date: ")
            violationMessage = input("enter reason for violation: ")
            fineAmount = input("enter fine amount: ")
            tno = input("give the ticket a unique id of the format : ")

            cursor.execute(
                "Insert into tickets({0}, {1}, {2}, {3}, {4})".format(tno, regno, fineAmount, violationMessage, violationDate)
            )
            print("successfully issued ticket\n")
        # end logic
        ##################################################################################


        # display output, then return to dashboard     

        # clear the window again
        SysCallManager.ReturnToDashboard()

    def findCarOwner(self):
        # allow the traffic officer to find a car owner
        # perform issue ticket steps
        cursor = sqlCursor.get_instance().get_cursor()
        ##################################################################################
        # issue ticket SQL logic goes here
        carMakes = input("enter car make(s), separate each by a space").split(" ")
        carModels = input("enter car model(s), separate each by a space").split(" ")
        carYears = input("enter car year(s), separate each by a space").split(" ")
        carColors = input("enter car color(s), separate each by a space").split(" ")
        carPlates = input("enter car plate(s), separate each by a space").split(" ")

        query = "Select r.fname, r.lname" \
                "From registrations As r, vehicles As v" \
                "Where r.vin = v.vin And "
        query += "("
        for make in range(len(carMakes)):
            if (make == 0):
                query += carMakes[make]
            else:
                query += "Or {}".format(carMakes[make])
        query += ") And ("
        for model in range(len(carModels)):
            if (model == 0):
                query += carModels[model]
            else:
                query += "Or {}".format(carModels[model])
        query += ") And ("
        for year in range(len(carYears)):
            if (year == 0):
                query += carYears[year]
            else:
                query += "Or {}".format(carYears[year])
        query += ") And ("
        for color in range(len(carColors)):
            if (color == 0):
                query += carColors[color]
            else:
                query += "Or {}".format(carColors[color])
        query += ") And ("
        for plate in range(len(carPlates)):
            if (plate == 0):
                query += carPlates[plate]
            else:
                query += "Or {}".format(carPlates[plate])
        query += ")"

        cursor.execute( query )

        if (len(queryResponse) == 4):
            # show make, model, year, color, and plate of all matches
            # let user select one
            pass
        else:
            # 
            pass
        # end logic
        ##################################################################################

        print("successfully found car owner\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

        