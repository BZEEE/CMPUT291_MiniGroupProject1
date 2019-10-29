
from TrafficOfficer import TrafficOfficer
from RegistryAgent import RegistryAgent
from AuthenticationManager import AuthenticationManager

class SessionManager():
    @staticmethod
    def enterSession():
        
        sessionManager = SessionManager()
        user = sessionManager.AuthenticateUser()
        # tests
        #user = TrafficOfficer("Traffic Officer", "John Doe")
        #user = RegistryAgent("Registry Agent", "Mike Myers")
        if (user != None):
            user.accessUserServices()
        else:
            print("session terminated due to unrecognized type of user\n")
        
        sessionManager.endSession()

    def endSession(self):
        # show closing messages for the user
        print("You have successfully logged out of the session\n")

    def AuthenticateUser(self):
        # dislpay login prompt for user
        validUID = False
        validPassword = False
        print("###################################################################################")
        print("########################   Welcome to the Login Screen   ##########################")
        print("###################################################################################\n")

        while not validUID: 
            # alternative implementation of a do-while loop in python
            uid = input("enter your uid: ")
            if (not isinstance(uid, str)):
                # return to beginning of authenticate while loop
                print("email entry is not of type(str)")
                continue
            if (not AuthenticationManager.checkIfUniqueIdExists(uid)):
                # return to beginning of authenticate while loop since email is not in database
                print("uid is not recognized in database, please ensure uid is correct")
                continue
            validUID = True

        while not validPassword:
            password = input("enter your password: ")
            if (not isinstance(password, str)):
                # return to beginning of authenticate while loop
                print("password entry is not of type(str)")
                continue
            if (not AuthenticationManager.checkIfPaswwordMatchesUniqueId(uid, password)):
                # return to beginning of authenticate while loop since email is not in database
                print("password is not correct")
                continue
            validPassword = True
        userType = AuthenticationManager.getUserType(uid)
        fullname = AuthenticationManager.getUserFullname(uid)
        if (userType == 'a'):
            return RegistryAgent(userType, fullname)
        elif (userType == 'o'):
            return TrafficOfficer(userType, fullname)
        else:
            print("Authenticated User is of an unrecognizable type\n")
            return None
            