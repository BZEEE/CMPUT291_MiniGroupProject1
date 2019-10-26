
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
    @staticmethod
    def iterate(dict):#creted to eliminate redundancy in 'registerBirth' and 'registerMarriage'
        #only dictionaries should be passed to this function.
        for item in dict:
            dict[item] = input(f'Enter {item}: ')
        return dict
    def registerBirth(self):
        # allow registry agent to register a birth
        # perform issue ticket steps
        cursor = sqlCursor.get_instance().get_cursor()
        columns = {'fname': None,'lname': None,'gender': None,'f_fname': None,'f_lname': None,'m_fname': None,\
            'm_lname': None,'bdate': None,'bplace': None}
        columns = self.iterate(columns)
        if self.check_person(columns['f_fname'],columns['f_lname']):#True if father is not in database
            print(f"Enter information about {columns['fname']} {columns['lname']}'s father'")
            columns2 = {'f_bdate': None,'f_bplace': None,'f_address': None,'f_phone': None}
            columns2 = self.iterate(columns2)
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{columns['f_fname']}','{columns['f_lname']}','{columns2['f_bdate']}','{columns2['f_bplace']}','{columns2['f_address']}','{columns2['f_phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except ValueError:
                print('Integrity Constraint')
        if self.check_person(columns['m_fname'],columns['m_lname']):#True if mother is not in database
            print(f"Enter information about {columns['fname']} {columns['lname']}'s mother'")
            columns3 = {'m_bdate': None,'m_bplace': None,'m_address': None,'m_phone': None}
            columns3 = self.iterate(columns3)
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{columns['m_fname']}','{columns['m_lname']}','{columns3['m_bdate']}','{columns3['m_bplace']}','{columns3['m_address']}','{columns3['m_phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except ValueError:
                print('Integrity Constraint')
        regno = UniqueIDManager.getUniqueRegistrationNumber('births')#generate unique number
        regdate = self.get_current_date()
        regplace = User.getUserCity()#get the city of the loged in user
        #getting the mothers phone and address
        cursor.execute("SELECT address,phone FROM persons WHERE fname=:m_fname AND lname=:m_lname;",\
            {'m_fname':columns['m_fname'],'m_lname':columns['m_lname']})
        m_info = cursor.fetchone()
        m_address = m_info[0]#mothers address
        m_phone = m_info[1]#mothers phone number
        ##################################################################################
        # register birt SQL logic goes here
        try:
            cursor.executescript(f'''INSERT INTO births VALUES ('{regno}','{columns['fname']}','{columns['lname']}','{regdate}','{regplace}','{columns['gender']}','{columns['f_fname']}','{columns['f_lname']}','{columns['m_fname']}','{columns['m_lname']}');
            INSERT INTO persons VALUES ('{columns['fname']}','{columns['lname']}','{columns['bdate']}','{columns['bplace']}','{m_address}','{m_phone}');''')
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
    def check_person(self,p_fname,p_lname):#helper function for registerBirth
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
    def get_current_date(self):#helper function for registerBirth
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute("SELECT date('now')")
        return cursor.fetchone()[0]
    #%%%%%%%%%
    def registerMarriage(self):
        cursor = sqlCursor.get_instance().get_cursor()
        # allow registry agent to register a marriage
        # perform issue ticket steps
        inputs = {'partner1_fname': None,'partner1_lname':None,'partner2_fname': None,'partner2_lname':None}
        inputs = self.iterate(inputs)
        regno = UniqueIDManager.getUniqueRegistrationNumber('marriages')#generate unique number
        regdate = self.get_current_date()
        regplace = User.getUserCity()#get the city of the loged in user
        if self.check_person(inputs['partner1_fname'],inputs['partner1_lname']):#True if partner_1 is not in database
            print(f"Enter the following information about {inputs['partner1_fname']} {inputs['partner1_lname']}")
            columns2 = {'bdate': None,'bplace': None,'address': None,'phone': None}
            columns2 = self.iterate(columns2)
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{inputs['partner1_fname']}','{inputs['partner1_lname']}','{columns2['bdate']}','{columns2['bplace']}','{columns2['address']}','{columns2['phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except ValueError:
                print('Integrity Constraint')
        if self.check_person(inputs['partner2_fname'],inputs['partner2_lname']):#True if partner2 is not in database
            print(f"Enter the following information about {inputs['partner2_fname']} {inputs['partner2_lname']}")
            columns3 = {'bdate': None,'bplace': None,'address': None,'phone': None}
            columns3 = self.iterate(columns3)
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{inputs['partner2_fname']}','{inputs['partner2_lname']}','{columns3['bdate']}','{columns3['bplace']}','{columns3['address']}','{columns3['phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except ValueError:
                print('Integrity Constraint')
        ##################################################################################
        # register marriage SQL logic goes here
        cursor.execute(f"INSERT INTO marriages VALUES ('{regno}','{regdate}','{regplace}','{inputs['partner1_fname']}','{inputs['partner1_lname']}','{inputs['partner2_fname']}','{inputs['partner2_lname']}')")
        sqlCursor.get_instance().get_connection().commit()
        # end logic
        ##################################################################################
        print("successfully registered marriage\n")
        input("press Enter to return to Dashboard")
        # clear the window again
        SysCallManager.clearWindow()
    @staticmethod
    def reg_exist(regno):#Will return True if registration exist
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute("SELECT expiry FROM registrations WHERE regno=:regno;",{'regno':regno})
        if cursor.fetchone() == None:
            return False
        return True
    def renewVehicleRegistration(self):
        # allow registry agent to renew their registration
        # perform issue ticket steps
        cursor = sqlCursor.get_instance().get_cursor()
        regno = input("Enter registry number: ")
        exist = not(self.reg_exist(regno))
        while exist:# check if registraion num exist
            print('Registration not found')
            option = input("Enter (1) to enter a different registry number\nEnter (2) to return to dashboard")
            if option == '1':
                exist = not(self.reg_exist(regno))
            else:
                SysCallManager.ReturnToDashboard()
        cursor.execute("SELECT expiry FROM registrations WHERE regno=:regno;",{'regno':regno})
        cur_expiry = cursor.fetchone()[0]
        cursor.execute(f"SELECT strftime('%s','now') - strftime('%s','{cur_expiry}');")#calculating time difference in unix timestamp
        ##################################################################################
        # renew vehicle registration SQL logic goes here
        if cursor.fetchone()[0] < 0:#registration is not expired
            new_date = str(int(cur_expiry[:4])+1)+(cur_expiry[4:])
            #slef.get_current_date returns an integer so need to convert it to a string to concatenate
            #will concatante first 4 letters of the string, which is the year, turn it into an integer add1 to it and then
            #turn it back to a string and concatinate it back to the rest of the dates.
            cursor.execute("UPDATE registrations SET expiry=:new_date WHERE regno=:regno;",{'new_date':new_date,'regno':regno})
            sqlCursor.get_instance().get_connection().commit()
        else:#registration is expired
            new_date = str(int(str(self.get_current_date())[:4])+1)+(cur_expiry[4:])
            #will concatante first 4 letters of the string, which is the year, turn it into an integer add1 to it and then
            #turn it back to a string and concatinate it back to the rest of the dates.
            cursor.execute("UPDATE registrations SET expiry=:new_date WHERE regno=:regno;",{'new_date':new_date,'regno':regno})
            sqlCursor.get_instance().get_connection().commit()

        # end logic
        ##################################################################################

        print("successfully renewed vehicle registration\n")
        input("press Enter to return to Dashboard")

        # clear the window again
        SysCallManager.clearWindow()

    def processBillOfSale(self):
        cursor = sqlCursor.get_instance().get_cursor()
        # allow rgistry agent to process a bill of sale
        # perform issue ticket steps
        inputs = {'vin_of_car':None,'firstname_of_current_owner':None,\
            'lastname_of_current_owner':None,'firstname_of_new_owner':None,\
                'lastname_of_new_owner':None,'New_plate_number':None}
        inputs = self.iterate(inputs)
        cursor.execute(f"SELECT fname,lname FROM registrations WHERE vin='{inputs['vin_of_car']}';")
        owner = cursor.fetchone() 
        if owner == None or (owner[0] != inputs['firstname_of_current_owner'] and owner[1] != inputs['lastname_of_current_owner']):
            #This will check if the most recent owner of the vehicle is the inputed current owner and if it isnt user will be returned to Dashboard
            print(f"The inputed vehicle with the vin number {inputs['vin_of_car']}is not currently owned by {inputs['firstname_of_current_owner']} {inputs['lastname_of_current_owner']}")
            SysCallManager.ReturnToDashboard()
        regno = UniqueIDManager.getUniqueRegistrationNumber('registrations')#generate unique number
        regdate = str(self.get_current_date())
        ##################################################################################
        # process bill of sale SQL logic goes here
        cursor.executescript(f'''UPDATE registrations SET expiry = '{self.get_current_date()}' WHERE vin = '{inputs['vin_of_car']}';
                                INSERT INTO registrations VALUES ('{regno}','{regdate}','{str(int(regdate[:4])+1)+regdate[4:]}',\
                                    '{inputs['New_plate_number']}','{inputs['vin_of_car']}','{inputs['firstname_of_new_owner']}',\
                                        '{inputs['lastname_of_new_owner']}');''')
        sqlCursor.get_instance().get_connection().commit()
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
        