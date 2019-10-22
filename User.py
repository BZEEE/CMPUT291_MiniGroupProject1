
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
