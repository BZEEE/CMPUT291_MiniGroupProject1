
from User import User
from SysCallManager import SysCallManager
from cursor import sqlCursor
from random import randint


class RegistryAgent(User):
    # inherit from base properties of user
    def __init__(self, uType, name):
        self.userType = uType
        self.fullname = name

    def getUserType(self):
        # super().getUserType()
        return self.userType

    def getUserFullName(self):
        # super().getUserFullName()
        return self.fullname

    def showGreeting(self):
        header = "###################################################################################"
        greeting = " Welcome, " + self.fullname + " "
        middleHeader = ""
        fillerLength = (len(header) - len(greeting)) // 2
        middleHeader += "#"
        for i in range(fillerLength - 1):
            middleHeader += "-"
        middleHeader += greeting
        for i in range(fillerLength - 1):
            middleHeader += "-"
        middleHeader += "#"

        print(header)
        print(middleHeader)
        print(header + "\n")

    def accessUserServices(self):
        SysCallManager.clearWindow()
        # super().accessUserServices()
        # show possible services for Registry Agent
        accessServices = True
        while (accessServices):
            self.showGreeting()
            print("###### Registry Agent Services Dashboard ######")
            print("Enter (1) to register a birth")
            print("Enter (2) to register a marriage")
            print("Enter (3) to renew vehicle registration")
            print("Enter (4) to process a bill of sale")
            print("Enter (5) to process a payment")
            print("Enter (6) to get a driver's abstract")
            print("Enter (7) to exit and log out of the session\n")
            response = input("please enter an action: ")
            print("\n")
            if (response == "1"):
                self.registerBirth()
            elif (response == "2"):
                self.registerMarriage()
            elif (response == "3"):
                self.renewVehicleRegistration()
            elif (response == "4"):
                self.processBillOfSale()
            elif (response == "5"):
                self.processPayment()
            elif (response == "6"):
                self.getDriverAbstract()
            elif (response == "7"):
                accessServices = False
            else:
                print("the action you selected is not recognized, try again\n")

    def registerBirth(self):
        # allow registry agent to register a birth
        # perform issue ticket steps
        columns = {'fname': None,'lname': None,'gender': None,'f_fname': None,'f_lname': None,'m_fname': None,'m_lname': None,'bdate': None,'bplace': None,'f_bdate': None,\
        'f_bplace': None,'f_address': None,'f_phone': None,'m_bdate': None,'m_bplace': None,'m_address': None,'m_phone': None}
        for items in columns:
            columns[item] = input(f'Enter {item}: ')
        if self.check_parents(columns['f_fname'],columns['f_lname']):#True if father is not in database
            self.conn.get_instance().get_cursor().execute("INSERT INTO persons(fname:f_fname,lname:f_lname,f_bdate:f_bdate,f_bplace:f_bplace,f_address:f_address,f_phone:f_phone)",{
                'f_fname':columns['f_fname'],'f_lname':columns['f_lname'],'f_bdate':columns['f_bdate'],'f_bplace':columns['f_bplace'],'f_address':columns['f_address'],'f_phone':columns['f_phone']})
            self.conn.get_instance().get_cursor().commit()
        if self.check_parents(columns['m_fname'],columns['m_lname']):#True if mother is not in database
            self.conn.get_instance().get_cursor().execute("INSERT INTO persons(fname:m_fname,lname:m_lname,m_bdate:m_bdate,m_bplace:m_bplace,m_address:m_address,m_phone:m_phone)",{
                'm_fname':columns['m_fname'],'m_lname':columns['m_lname'],'m_bdate':columns['m_bdate'],'m_bplace':columns['m_bplace'],'m_address':columns['m_address'],'m_phone':columns['m_phone']})
            self.conn.get_instance().get_cursor().commit()
        regno = random.randint(1,100000)
        regdate = self.get_current_date()
        regplace = User.getUserCity
        while self.check_id(regno):#will check if id already exist
            regno = random.randint(1,100000)
        
        ##################################################################################
        # register birt SQL logic goes here
        self.conn.get_instance().get_cursor().executescript('''INSERT INTO births(
            regno,fname,lname,regdate,regplace,gender,f_fname.f_lname,m_fname,m_lname
        );
        INSERT INTO persons(
            fname,lname,bdate,bplace,m_address,m_phone
        );''',{'fname':columns['fname'],'lname':columns['lname'],'regno':columns['regno'],'regdate':columns['regdate'],'regplace':columns['regplace'],'gender':columns['gender'],'f_fname':columns['f_fname'],'f_lname':columns['f_lname'],\
            'm_fname':columns['m_fname'],'bdate':columns['bdate'],'bplace':columns['bplace'],'m_lname':columns['m_lname'],'m_address':columns['m_address'],'m_phone':columns['m_phone']})
        # end logic
        ##################################################################################

        print("successfully registered birth\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()
    #%%%%%%%
    #The following function can be made into their own seperate file if needed
    def check_parents(self,p_fname,p_lname):#helper function for registerBirth
        self.conn.get_instance().get_cursor().execute('SELECT fname,lname FROM persons WHERE fname=:p_fname AND lname=:p_lname;',{"p_fname":p_fname,"p_lname":p_lname})
        output = self.conn.get_instance().get_cursor().fetchone()
        if output[0] != None:
            return False#need to know what the query returns when it returns an empty tuple
        return True
    def check_id(self,num):#helper function for registerBirth
        #will check if 'num' is already an existing id
        self.conn.get_instance().get_cursor().execute('SELECT regno FROM births WHERE regno =:num;',{'num':num})
        output = self.conn.get_instance().get_cursor().fetchone()[0]
        if output[0] != None:#need to check if sql outputs None for empty tuples
            return True#id already exist
        return False
    def get_current_date(self):
        self.conn.get_instance().get_cursor().execute("SELECT date('now')")
        return self.conn.get_instance().get_cursor().fetchone()[0]
    #%%%%%%%%%
    def registerMarriage(self):
        # allow registry agent to register a marriage
        # perform issue ticket steps
        ##################################################################################
        # register marriage SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully registered marriage\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def renewVehicleRegistration(self):
        # allow registry agent to renew their registration
        # perform issue ticket steps

        ##################################################################################
        # renew vehicle registration SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully renewed vehicle registration\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def processBillOfSale(self):
        # allow rgistry agent to process a bill of sale
        # perform issue ticket steps

        ##################################################################################
        # process bill of sale SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully processed bill of sale\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def processPayment(self):
        # allow registry agent to process a payment
        # perform issue ticket steps

        ##################################################################################
        # process payment SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully processed payment\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def getDriverAbstract(self):
        # allow registry agent to get a driver abstract
        # perform issue ticket steps

        ##################################################################################
        # get driver abstract SQL logic goes here


        # end logic
        ##################################################################################

        print("successfully retrieved driver abstract\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()
        