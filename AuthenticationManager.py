
from cursor import sqlCursor
class AuthenticationManager:
    validPassword = None 
    validUid = None
    @classmethod
    def store_uid(cls,uid):
        cls.validUid = uid
    @classmethod
    def store_pass(cls,pwd):
        cls.validPassword = pwd
    @staticmethod
    def checkIfUniqueIdExists(uid):
        # return true or false depending if uid exists in database
        
        # get tuple list of all uid's in users
        cursor = sqlCursor.get_instance().get_cursor()
        cursorResponse = cursor.execute(
            '''Select uid  
            From users;
           '''
        )
        cursorResponse = cursor.fetchall()
        match = False
        if (cursorResponse == None):
            return match
        else:
            for userID in cursorResponse:
                if (userID[0].upper() == uid.upper()):
                    AuthenticationManager.store_uid(uid) #saving this to be able to refer to the current user,this is saved on User.py
                    match = True

            return match

    @staticmethod
    def checkIfPaswwordMatchesUniqueId(uid, password):
        # return true if password matches correctly with unique id
        cursor = sqlCursor.get_instance().get_cursor()
        cursorResponse = cursor.execute(
            "Select pwd " \
            "From users " \
            "Where uid =:uid " ,{'uid':uid}
        )
        cursorResponse = cursor.fetchall()

        if (cursorResponse == None):
            return False
        else:
            if (cursorResponse[0][0] == password):
                AuthenticationManager.store_pass(password) #saving this to be able to refer to the current user, this is saved on User.py
            return (cursorResponse[0][0] == password)
    
    @staticmethod
    def getUserType(uid):
        # return utype associated with user
        cursor = sqlCursor.get_instance().get_cursor()
        cursorResponse = cursor.execute(
            '''Select utype  
            From users  
            Where uid =:uid;''',{'uid':uid}
        )
        cursorResponse = cursor.fetchall()

        if (cursorResponse == None):
            return None
        else:
            return cursorResponse[0][0]

    @staticmethod
    def getUserFullname(uid):
        # return fullname (string) of user 
        cursor = sqlCursor.get_instance().get_cursor()
        cursorResponse = cursor.execute(
            '''Select fname, lname 
            From users 
            Where uid =:uid;''',{'uid':uid}
        )
        cursorResponse = cursor.fetchall()

        if (cursorResponse == None):
            return None
        else:
            return cursorResponse[0][0] + " " + cursorResponse[0][1]
