

class UniqueIDManager:
    __singleton = None
    __tno = 0
    __regno = 0
    __vin = 100
    @staticmethod
    def getInstance():
        if (UniqueIDManager.__singleton == None):
            UniqueIDManager.__singleton = UniqueIDManager()
            return UniqueIDManager.__singleton
        else:
            return UniqueIDManager.__singleton

    def getUniqueTicketNumber(self):
        copy = self.__tno    # make a copy of the ticket number counter
        self.__tno += 1      # increment
        return copy     # return copy of tno before it was incremented
    
    def getUniqueRegistrationNumber(self):
        copy = self.__regno    # make a copy of the registration number counter
        self.__regno += 1      # increment
        return copy       # return copy of regno before it was incremented

    def getUniqueVehicleInsuranceNumber(self):
        copy = self.__vin                 # make a copy of the vehicle insurance numer number counter
        self.__vin += 1                   # increment
        return "U" + str(copy)       # return copy of vehicle insurance number before it was incremented
