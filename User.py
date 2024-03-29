
# required to implement abstract classes
from abc import ABC, abstractmethod 
from cursor import sqlCursor
from AuthenticationManager import AuthenticationManager

#from SessionManager import SessionManager
class User:
    # base class representing shared data amongst al users
    # each specific type of User must implement the services available to them in their own class
    def __init__(self, uType, name):
        self.userType = uType
        self.fullname = name
    @abstractmethod
    def getUserType(self):
        # each user must be able to reveal its type
        return 
    @abstractmethod
    def getUserFullName(self):
        # each user must be able to reveal its fullname
        return 
    
    @abstractmethod
    def accessUserServices(self):
        # show the services available for a specific user, implmented differently by each possible user
        pass

    def displayFormattedQueryResponse(self, queryResponse, start, end, columnTitles):
        maxLength = 20
        for title in columnTitles:
            i = len(title)
            print(" | ", end="")
            print (title, end="")
            for j in range(maxLength - i):
                print(" ", end="")
        print(" | ")

        for tuples in queryResponse:
            for k in range((maxLength + 3) * len(tuples) + 3):
                print("-", end="")
            print("")
            print(" | ", end="")
            for col in range(start, end + 1):
                i = len(str(tuples[col]))
                print(tuples[col], end="")
                for j in range(maxLength - i):
                    print(" ", end="")
                print(" | ", end="")
            print("")

        # this method has the same behaviour for everyprint
        print("\n")
    @staticmethod
    def getUserCity():
        #pass in created uid and pwd
        cursor = sqlCursor.get_instance().get_cursor()
        try:
            cursor.execute("SELECT city FROM users WHERE uid=:uid AND pwd=:pwd",{'uid':AuthenticationManager.validUid,'pwd':AuthenticationManager.validPassword})
        except sqlCursor.get_error() as e:
            print("error when retieving the user's city from the database")
            return
        return cursor.fetchone()[0]
        
