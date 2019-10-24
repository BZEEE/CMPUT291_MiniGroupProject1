
# required to implement abstract classes
from abc import ABC, abstractmethod 
from cursor import sqlCursor
class User:
    # base class representing shared data amongst al users
    # each specific type of User must implement the services available to them in their own class
    conn = sqlCursor()
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
    def getUserCity(self,uid,pwd):
        #pass in created uid and pwd
        self.conn.get_instance().get_cursor().execute("SELECT city FROM users WHERE uid=:uid AND pwd=:pwd",{'uid':uid,'pwd':pwd})
        return self.conn.get_instance().get_cursor().fetchone()[0]
