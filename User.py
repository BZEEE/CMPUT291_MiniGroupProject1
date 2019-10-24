
# required to implement abstract classes
from abc import ABC, abstractmethod 

class User:
    # base class representing shared data amongst al users
    # each specific type of User must implement the services available to them in their own class
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

    def displayFormattedQueryResponse(self, queryResponse, start, end, *columnTitles):
        maxLength = 20
        for title in columnTitles:
            i = len(title)
            print(" | ", end="")
            print (title, end="")
            for j in range(maxLength - i):
                print(" ", end="")
        print(" | ")


        for tuples in queryResponse:
            for k in range(26 * len(tuples)):
                print("-", end="")
            print("")
            print(" | ", end="")
            for col in range(start, end + 1):
                i = len(tuples[col])
                print(tuples[col], end="")
                for j in range(maxLength - i):
                    print(" ", end="")
                print(" | ", end="")
            print("")

        # this method has the same behaviour for every user; Registry Agent, Traffic Officer, etc
        print("\n")
