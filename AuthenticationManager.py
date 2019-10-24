
from cursor import sqlCursor

class AuthenticationManager:
    @staticmethod
    def checkIfUniqueIdExists(uid):
        # return true or false depending if uid exists in database
        
        # get tuple list of all uid's in users
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursorResponse = cursor.execute(
            "Select uid " \
            "From users"
        )
        conn.commit()
        cursorResponse = cursor.fetchall()

        match = False
        if (cursorResponse == None):
            return match
        else:
            for userID in cursorResponse:
                if (userID[0].upper() == uid.upper()):
                    match = True

            return match

    @staticmethod
    def checkIfPaswwordMatchesUniqueId(uid, password):
        # return true if password matches correctly with unique id
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursorResponse = cursor.execute(
            "Select pwd " \
            "From users " \
            "Where uid=:uid", {"uid": uid}
        )

        conn.commit()
        cursorResponse = cursor.fetchall()
        print(cursorResponse)

        if (cursorResponse == None):
            return False
        else:
            return (cursorResponse[0][0] == password)
    
    @staticmethod
    def getUserType(uid):
        # return utype associated with user
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursorResponse = cursor.execute(
            "Select utype " \
            "From users " \
            "Where uid=:uid", {"uid": uid}
        )
        conn.commit()
        cursorResponse = cursor.fetchall()

        if (cursorResponse == None):
            return None
        else:
            return cursorResponse[0][0]

    @staticmethod
    def getUserFullname(uid):
        # return fullname (string) of user 
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursorResponse = cursor.execute(
            "Select fname, lname " \
            "From users " \
            "Where uid=:uid", {"uid": uid}
        )
        conn.commit()
        cursorResponse = cursor.fetchall()

        if (cursorResponse == None):
            return None
        else:
            return cursorResponse[0][0] + " " + cursorResponse[0][1]
