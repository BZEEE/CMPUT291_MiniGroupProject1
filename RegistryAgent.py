
from User import User
from SysCallManager import SysCallManager
from cursor import sqlCursor
from UniqueIDManager import UniqueIDManager

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
        cursor = sqlCursor.get_instance().get_cursor()
        columns = {'fname': None,'lname': None,'gender': None,'f_fname': None,'f_lname': None,'m_fname': None,\
            'm_lname': None,'bdate': None,'bplace': None,'f_bdate': None,'f_bplace': None,'f_address': None,\
                'f_phone': None,'m_bdate': None,'m_bplace': None,'m_address': None,'m_phone': None}
        for items in columns:
            columns[items] = input(f'Enter {items}: ')
        #-----------
        #test data
        '''
        columns = {'fname': 'Ivan','lname': 'Penales','gender': "male",'f_fname': "Benny",'f_lname': "Penales",\
            'm_fname': "Polly",'m_lname': "Penales",'bdate': "04/15/1997",'bplace': "Phillipines",'f_bdate': "02/15/1969",\
        'f_bplace': "Phillipines",'f_address': "Phillipines",'f_phone': "403",'m_bdate': "05/11/1969",'m_bplace': "Phillipines",\
            'm_address': "Phillipines",'m_phone': "913"}
        '''
        #----------
        if self.check_parents(columns['f_fname'],columns['f_lname']):#True if father is not in database
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{columns['f_fname']}','{columns['f_lname']}','{columns['f_bdate']}','{columns['f_bplace']}','{columns['f_address']}','{columns['f_phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except ValueError:
                print('Integrity Constraint')
        if self.check_parents(columns['m_fname'],columns['m_lname']):#True if mother is not in database
            cursor.execute(f'''INSERT INTO persons VALUES 
            ('{columns['m_fname']}','{columns['m_lname']}','{columns['m_bdate']}','{columns['m_bplace']}','{columns['m_address']}','{columns['m_phone']}');''')
            sqlCursor.get_instance().get_connection().commit()
        regno = UniqueIDManager.getUniqueRegistrationNumber()
        regdate = self.get_current_date()
        regplace = User.getUserCity()
        ##################################################################################
        # register birt SQL logic goes here
        try:
            cursor.executescript(f'''INSERT INTO births VALUES ('{regno}','{columns['fname']}','{columns['lname']}','{regdate}','{regplace}','{columns['gender']}','{columns['f_fname']}','{columns['f_lname']}','{columns['m_fname']}','{columns['m_lname']}');
            INSERT INTO persons VALUES ('{columns['fname']}','{columns['lname']}','{columns['bdate']}','{columns['bplace']}','{columns['m_address']}','{columns['m_phone']}');''')
            sqlCursor.get_instance().get_connection().commit()
        except ValueError:
            print('Integrity Constraint')
        # end logic
        ##################################################################################

        print("successfully registered birth\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()
    #%%%%%%%
    #The following function can be made into their own seperate file if needed
    def check_parents(self,p_fname,p_lname):#helper function for registerBirth
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute('SELECT fname,lname FROM persons WHERE fname=:p_fname AND lname=:p_lname;',{"p_fname":p_fname,"p_lname":p_lname})
        output = cursor.fetchone()
        if output != None:
            return False#need to know what the query returns when it returns an empty tuple
        return True
    def check_id(self,num):#helper function for registerBirth
        #will check if 'num' is already an existing id
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute('SELECT regno FROM births WHERE regno =:num;',{'num':num})
        output = cursor.fetchone()
        if output != None:#need to check if sql outputs None for empty tuples
            return True#id already exist
        return False
    def get_current_date(self):
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute("SELECT date('now')")
        return cursor.fetchone()[0]
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
        