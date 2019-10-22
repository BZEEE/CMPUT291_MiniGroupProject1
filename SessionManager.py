
from TrafficOfficer import TrafficOfficer
from RegistryAgent import RegistryAgent
from AuthenticationManager import AuthenticationManager

class SessionManager:
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
        validEmail = False
        validPassword = False

        while not validEmail: 
            # alternative implementation of a do-while loop in python
            uid = input("enter your email: ")
            if (not isinstance(uid, str)):
                # return to beginning of authenticate while loop
                print("email entry is not of type(str)")
                continue
            if (not AuthenticationManager.checkIfUniqueIdExists(uid)):
                # return to beginning of authenticate while loop since email is not in database
                print("email is not recognized in database, please ensure email is correct\n")
                continue
            validEmail = True

        while not validPassword:
            password = input("enter your password: ")
            if (not isinstance(password, str)):
                # return to beginning of authenticate while loop
                print("password entry is not of type(str)")
                continue
            if (AuthenticationManager.checkIfPaswwordMatchesUniqueId(uid, password)):
                # return to beginning of authenticate while loop since email is not in database
                print("password is not correct, please ensure email is correct\n")
                continue
            validPassword = True

        userType = AuthenticationManager.getUserType(uid)
        fullname = AuthenticationManager.getUserFullname(uid)
        if (userType == "Registry Agent"):
            return RegistryAgent(userType, fullname)
        elif (userType == "Traffic Officer"):
            return TrafficOfficer(userType, fullname)
        else:
            print("Authenticated User is of an unrecognizable type\n")
            return None
            