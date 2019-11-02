from cursor import sqlCursor

class UniqueIDManager:
    __tno = 0
    __regno = 0
    __vin = 100
    @staticmethod
    def getUniqueTicketNumber():
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursor.execute("SELECT max(tno) FROM tickets;")
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
        try:
            cursor.execute("SELECT max(regno) FROM {};".format(table))
            conn.commit()
        except sqlCursor.get_error() as e:
            print("Error when fetching maximum regid from table")
        val = cursor.fetchone()
        if val == None:
            val = 0
        elif val[0] == None:
            val = 0
        else:
            val = int(val[0]) + 1#this is the current regno to be used
        return val       

    @staticmethod
    def getUniqueVehicleInsuranceNumber():     
        cursor = sqlCursor.get_instance().get_cursor()
        conn = sqlCursor.get_instance().get_connection()
        cursor.execute("SELECT max(vin) FROM vehicles;")
        output = cursor.fetchone()[0]
        if output == None: output = 'U100'
        output = int(output[1:]) + 1
        return "U" + str(output)       # return copy of vehicle insurance number before it was incremented
