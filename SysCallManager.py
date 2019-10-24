
import os
import time

class SysCallManager:
    @staticmethod
    def clearWindow():
        os.system("cls")

    @staticmethod 
    def ReturnToDashboard():
        input("press Enter to return to Dashboard")
        print("\r")
        i = 3
        while (i > 0):
            print("Returning To Dashboard in {}".format(i))
            time.sleep(1)
            i -= 1
            print("\r") # delete a single line from the command line
        
        os.system("cls")

        