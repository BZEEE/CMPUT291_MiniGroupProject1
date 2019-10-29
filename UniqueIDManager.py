from cursor import sqlCursor

class UniqueIDManager:
    __singleton = None
    __tno = 0
    __regno = 0
    __vin = 100
    @staticmethod
    def getUniqueTicketNumber():
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursor.execute(f"SELECT max(tno) FROM tickets;")
        conn.commit()
        response = cursor.fetchone()
        if response == None:
            response = 0
        else:
            response = int(response[0]) + 1
        return response
    
    @staticmethod
    def getUniqueRegistrationNumber(table):
        #pass in the specific table which we are creating a new id in in order to make sure that it is unique in that table
        copy = UniqueIDManager.__regno   # make a copy of the registration number counter
        if copy == 0: #query to see if theres a registration number in the database already
            cursor = sqlCursor.get_instance().get_cursor()
            conn = sqlCursor.get_instance().get_connection()
            cursor.execute(f"SELECT max(regno) FROM {table};")
            conn.commit()
            val = cursor.fetchone()
            if val[0] == None:
                None
            else:
                copy = val[0] + 1#this is the current regno to be used
                UniqueIDManager.__regno = val[0] + 2#this is the next regno to be used
        UniqueIDManager.__regno += 1      # increment
        return copy       # return copy of regno before it was incremented

    @staticmethod
    def getUniqueVehicleInsuranceNumber():
        copy = UniqueIDManager.__vin                 # make a copy of the vehicle insurance numer number counter
        UniqueIDManager.__vin += 1                   # increment
        return "U" + str(copy)       # return copy of vehicle insurance number before it was incremented
