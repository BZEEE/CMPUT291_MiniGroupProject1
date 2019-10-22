
import os
import time

class SysCallManager:
    @staticmethod
    def clearWindow():
        os.system("cls")

    @staticmethod 
    def ReturnToDashboard():
        i = 5
        while (i > 0):
            print("Returning To Dashboard in {}".format(i))
            time.sleep(1)
            i -= 1
            print("\r") # delete a single line from the command line
        
        os.system("cls")

        