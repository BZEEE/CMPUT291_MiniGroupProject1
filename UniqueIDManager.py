from cursor import sqlCursor

class UniqueIDManager:
    __tno = 0
    __regno = 0
    __vin = 100
    @staticmethod
    def getUniqueTicketNumber():
        copy = UniqueIDManager.__tno    # make a copy of the ticket number counter
        UniqueIDManager.__tno += 1      # increment
        return copy     # return copy of tno before it was incremented
    
    @staticmethod
    def getUniqueRegistrationNumber():
        copy = UniqueIDManager.__regno   # make a copy of the registration number counter
        if copy == 0: #query to see if theres a registration number in the database already
            cursor = sqlCursor.get_instance().get_cursor()
            cursor.execute("SELECT max(regno) FROM births;")
            val = cursor.fetchone()
            if val != None and val[0] >= 0:
                copy = val[0] + 1#this is the current regno to be used
                UniqueIDManager.__regno = val[0] + 2#this is the next regno to be used
        UniqueIDManager.__regno += 1      # increment
        return copy       # return copy of regno before it was incremented

    @staticmethod
    def getUniqueVehicleInsuranceNumber():
        copy = UniqueIDManager.__vin                 # make a copy of the vehicle insurance numer number counter
        UniqueIDManager.__vin += 1                   # increment
        return "U" + str(copy)       # return copy of vehicle insurance number before it was incremented
