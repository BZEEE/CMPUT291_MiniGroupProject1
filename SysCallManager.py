
import os
import time

class SysCallManager:
    @staticmethod
    def clearWindow():
        os.system("cls")

    @staticmethod 
    def ReturnToDashboard():
        input("press Enter to return to Dashboard")
        i = 3
        while (i > 0):
            print("Returning To Dashboard in {}".format(i), end="")
            print("\r", end="")
            time.sleep(1)
            i -= 1
        
        os.system("cls")

        