

class UniqueIDManager:
    __tno = 0
    __regno = 0
    __vin = 100
    @staticmethod
    def getUniqueTicketNumber():
        copy = __tno    # make a copy of the ticket number counter
        __tno += 1      # increment
        return copy     # return copy of tno before it was incremented
    
    @staticmethod
    def getUniqueRegistrationNumber():
        copy = __regno    # make a copy of the registration number counter
        __regno += 1      # increment
        return copy       # return copy of regno before it was incremented

    @staticmethod
    def getUniqueVehicleInsuranceNumber():
        copy = __vin                 # make a copy of the vehicle insurance numer number counter
        __vin += 1                   # increment
        return "U" + str(copy)       # return copy of vehicle insurance number before it was incremented
