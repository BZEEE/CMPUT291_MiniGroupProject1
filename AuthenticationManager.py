
from cursor import sqlCursor

class AuthenticationManager:
    @staticmethod
    def checkIfUniqueIdExists(uid):
        # return true or false depending if uid exists in database
        
        # get tuple list of all uid's in users
        cursor = sqlCursor.get_instance().get_cursor()
        cursorResponse = cursor.execute(
            "Select uid" \
            "From users"
        )
        match = False
        for userID in cursorResponse:
            if (userID.upper() == uid.upper()):
                match = True

        return match

    @staticmethod
    def checkIfPaswwordMatchesUniqueId(uid, password):
        # return true if password matches correctly with unique id
        cursor = sqlCursor.get_instance().get_cursor()
        cursorResponse = cursor.execute(
            "Select pwd" \
            "From users" \
            "Where uid = " + uid
        )

        return (cursorResponse == password)
    
    @staticmethod
    def getUserType(uid):
        # return utype associated with user
        pass

    @staticmethod
    def getUserFullname(uid):
        # return fullname (string) of user 
        cursor = sqlCursor.get_instance().get_cursor()
        cursorResponse = cursor.execute(
            "Select fname, lname" \
            "From users" \
            "Where uid = " + uid
        )

        return cursorResponse[0] + " " + cursorResponse[1]
