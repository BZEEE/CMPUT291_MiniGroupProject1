from cursor import sqlCursor

class UniqueIDManager:
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

        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursor.execute(f"SELECT max(regno) FROM {table};")
        conn.commit()
        val = cursor.fetchone()
        if val[0] == None:
            val = 0
        else:
            val = val[0] + 1#this is the current regno to be used
        return val       # return copy of regno before it was incremented

    @staticmethod
    def getUniqueVehicleInsuranceNumber():     
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursor.execute("SELECT max(vin) FROM vehicles;")
        output = cursor.fetchne()[0]
        output = int(output[1:]) + 1
        return "U" + str(output)       # return copy of vehicle insurance number before it was incremented
