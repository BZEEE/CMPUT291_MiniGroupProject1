
from User import User
from SysCallManager import SysCallManager
from cursor import sqlCursor
from UniqueIDManager import UniqueIDManager
import sqlite3

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
    #=================================================================================
    #THE FOLLOWING METHODS ARE FOR ERROR CHECKING AND ARE MODULAR ENOUGH TO EXIST IN A FILE OF ITS OWN
    @staticmethod
    def iterate(dict):#created to eliminate redundancy 
        #only dictionaries should be passed to this function.
        #returns a mutated dictionary object
        for item in dict:
            dict[item] = input(f'Enter {item}: ').strip()
        return dict
    @staticmethod
    def is_string(inp):#checks if input is string
        #returns a boolean value dpending on the format of the string.
        #This function is used over pyton built-ins since python built-ins
        #classifies a string as a non-didgit as long as it contains at-least
        #one non-didgit character.
        if inp == '':return False#cant be null
        for item in inp:
            if item.isdigit() or inp == '':
                return False
        return True
    @staticmethod
    def is_phone(inp):#checks if phone number is properly formatted
        #returns True if phone is of proper format
        if (inp.replace('-','')).isdigit():return True
        #the '-' is simply removed and the string is supposed to only contain digits.
        else:return False
    @staticmethod
    def is_date(inp):#checks date format is correct
        #inp is of type string.
        #dates not of the FROM 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS'  where Y,M,D,H.M, and S are integers, will make this function return false
        if len(inp) == 10:# this means that the date format is of the form 'YYYY-MM-DD'
            if RegistryAgent.date_form(inp):return True
            return False
        elif len(inp) == 19:#date might include the seconds and hour hence its of the form 'YYYY-MM-DD HH:MM:SS'
            inp = inp.strip()#take out all the spaces
            if RegistryAgent.date_form(inp):#will return True if the first 10 characters of date is correct
                for item in range(10,18):
                    if item == 13 or item == 16:
                        if inp[item] == ':':continue
                        else:return False
                    else:#everything that reaches this block must be a digit
                        if (inp[item]).isdigit():continue
                        else:return False
                return True
            else:return False
        else:return False#if date length is not 10 or 19 then it is incorrect
    @staticmethod
    def inp_check(cont,attr,prop_form):#this function is to make sure that the user enters a correct format when being re_prompt
        '''
        cont: This argument is the container for the data being mutated. This will be a dictionary.
        attr: This is the dictionary key used to refer to the value that is eing checked
        prop_form: This is one of the four functions above, each one is used to check if an input with a specific
        type has the proper format.

        In addition to mutating 'cont' this function will return a boolean value depending wether the user chooses 
        to terminate the program while this function is still running.
        ''' 
        output = True
        while not(prop_form(cont[attr])):#prop_form is one of the four functions above
            #and cont[attr] is the inproperly formated input
            if isinstance(cont[attr],list):#proper input can be never be a list since out database only accepts int,char, and date
                SysCallManager.ReturnToDashboard()
                output = False
                break
            if RegistryAgent.re_input(cont,attr) == False:
                SysCallManager.ReturnToDashboard()
                return False#this will terminate the for loop in 'iterate_check'
        return output#need to return a boolean so we can terminate the outer function if needed
    @staticmethod
    def re_input(cont,attr):#container is where the data is saved 
        '''
        cont: This argument is the container for the data being mutated. This will be a dictionary.
        attr: This is the dictionary key used to refer to the value that is eing checked

        This function will return a boolean value which depends on wether the user chose to terminate the code
        '''
        option = input(f"{attr} has an incorrect format. Press 'Y' to re-enter a new {attr} or 'N' to return to dashboard: ")
        while option.lower() != 'n': 
            if option.lower() == 'y':
                cont[attr] = input(f"Enter new {attr}: ")
                return
            option = input(f"{attr} has an incorrect format. Press 'Y' to re-enter a new {attr} or 'N' to return to dashboard: ")
        if option.lower() == 'n':cont[attr] = ['']#if the outside loop from 'inp_check' reads this it will break and return to dashboard  
        return False#will terminate the outer loop inp_check instantly
    @staticmethod
    def date_form(inp):#this is a helper function for 'is_date' that checks the first ten characters of a date.
        #This function will return a boolean value depending on the format of 'inp'
        for item in range(0,10):
                if item == 4 or item == 7:#inp[4] and inp[7] are supposed t be '-' if its in the proper format
                    if inp[item] == '-':continue
                    else:return False
                else:#everything that reaches this block must be a digit
                    if inp[item].isdigit():continue
                    else:return False
        return True
    @staticmethod
    def iterate_check(inp,prop_form):
        '''
        inp: is the dictionary object containing inputs from the user
        prop_form: is a list object containing what formats should be inserted to sqlite

        This function does not return anything.Rather it mutates the inp object by calling other functions.
        '''
        keys = list(inp.keys())#list of dictionary keys which are columns
        for item in range(0,len(inp)):#inp and prop_form are indexed so that the 
            #index of the 'proper format' in prop_form corresponds to the proper format of
            #the user's input contained in 'inp'.
            if prop_form[item] == 'str':
                if RegistryAgent.inp_check(inp,keys[item],RegistryAgent.is_string) == False:return False
            elif prop_form[item] == 'phone':
                if RegistryAgent.inp_check(inp,keys[item],RegistryAgent.is_phone) == False:return False
            elif prop_form[item] == 'date':
                if RegistryAgent.inp_check(inp,keys[item],RegistryAgent.is_date) == False:return False
    #=================================================================================
    #================================================================================
    #THE FOLLOWING ARE HELPER FUNCTIONS
    def check_person(self,p_fname,p_lname):#helper function for registerBirth
        #queries to check if the person is in the database.
        #return a boolean dpending on the pressence of 'p_fname' 'p_lname' in the database
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute("SELECT fname,lname FROM persons WHERE fname=:p_fname AND lname=:p_lname;",{"p_fname":p_fname,"p_lname":p_lname})
        output = cursor.fetchone()
        if output != None:
            return False#need to know what the query returns when it returns an empty tuple
        return True
    def check_id(self,num):#helper function for registerBirth
        #will check if 'num' is already an existing id
        #returns a boolean depending on the pressence of the id 'num' in the database
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute('SELECT regno FROM births WHERE regno =:num;',{'num':num})
        output = cursor.fetchone()
        if output != None:#need to check if sql outputs None for empty tuples
            return True#id already exist
        return False
    def get_current_date(self):#helper function for registerBirth
        #This function queries the current date from sql and returns it
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute("SELECT date('now')")
        return cursor.fetchone()[0]
    @staticmethod
    def reg_exist(regno):#Will return True if registration exist
        regno = regno.strip()
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute("SELECT expiry FROM registrations WHERE regno=:regno;",{'regno':regno})
        if cursor.fetchone() == None:
            return False
        return True
    #====================================================================
    def registerBirth(self):
        '''
        This function does not return anything it simplies stores the inputed,or possibly generated, values
        into the database.
        '''
        # allow registry agent to register a birth
        # perform issue ticket steps
        cursor = sqlCursor.get_instance().get_cursor()
        columns = {'fname': None,'lname': None,'gender': None,'f_fname': None,'f_lname': None,'m_fname': None,\
            'm_lname': None,'bdate': None,'bplace': None}
        columns = self.iterate(columns)#asks for user inputs
        prop_form = ['str','str','str','str','str','str','str','date','str']#error checking
        if self.iterate_check(columns,prop_form) == False:return#if this is true it means user returned to dashboard
        if self.check_person(columns['f_fname'],columns['f_lname']):#True if father is not in database
            print(f"Enter information about {columns['fname']} {columns['lname']}'s father'")
            columns2 = {'f_bdate': None,'f_bplace': None,'f_address': None,'f_phone': None}
            columns2 = self.iterate(columns2)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if self.iterate_check(columns2,prop_form) == False:return#is this is true it means user returned to dashboard
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{columns['f_fname']}','{columns['f_lname']}','{columns2['f_bdate']}','{columns2['f_bplace']}','{columns2['f_address']}','{columns2['f_phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except sqlite3.Error as e:
                print(f"error when inserting details of {columns['f_fname']} {columns['f_lname']} into the database")
        if self.check_person(columns['m_fname'],columns['m_lname']):#True if mother is not in database
            print(f"Enter information about {columns['fname']} {columns['lname']}'s mother'")
            columns3 = {'m_bdate': None,'m_bplace': None,'m_address': None,'m_phone': None}
            columns3 = self.iterate(columns3)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if self.iterate_check(columns3,prop_form) == False:return#is this is true it means user returned to dashboard
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{columns['m_fname']}','{columns['m_lname']}','{columns3['m_bdate']}','{columns3['m_bplace']}','{columns3['m_address']}','{columns3['m_phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except sqlite3.Error as e:
                    print(f"error when inserting details of {columns['m_fname']} {columns['m_lname']} into the database")
        regno = UniqueIDManager.getUniqueRegistrationNumber('births')#generate unique number
        regdate = self.get_current_date()
        regplace = User.getUserCity()#get the city of the loged in user
        #getting the mothers phone and address
        try:
            cursor.execute("SELECT address,phone FROM persons WHERE fname=:m_fname AND lname=:m_lname;",\
            {'m_fname':columns['m_fname'],'m_lname':columns['m_lname']})
        except sqlite3.Error as e:
            print(f"error when retrieving data about {columns['m_fname']} {columns['m_lname']} ")
        m_info = cursor.fetchone()
        m_address = m_info[0]#mothers address
        m_phone = m_info[1]#mothers phone number
        ##################################################################################
        # register birt SQL logic goes here
        try:
            cursor.executescript(f'''INSERT INTO births VALUES ('{regno}','{columns['fname']}','{columns['lname']}','{regdate}','{regplace}','{columns['gender']}','{columns['f_fname']}','{columns['f_lname']}','{columns['m_fname']}','{columns['m_lname']}');
            INSERT INTO persons VALUES ('{columns['fname']}','{columns['lname']}','{columns['bdate']}','{columns['bplace']}','{m_address}','{m_phone}');''')
            sqlCursor.get_instance().get_connection().commit()
        except sqlCursor.get_error() as e:
            print(f"error when inserting details of {columns['fname']} {columns['lname']} into the database")
        # end logic
        ##################################################################################
        print("successfully registered birth\n")
        SysCallManager.ReturnToDashboard()
        return
    def registerMarriage(self):
        '''
        This function does not return anything it simply inserts inputed or generated values into the database.
        '''
        cursor = sqlCursor.get_instance().get_cursor()
        # allow registry agent to register a marriage
        # perform issue ticket steps
        inputs = {'partner1_fname': None,'partner1_lname':None,'partner2_fname': None,'partner2_lname':None}
        inputs = self.iterate(inputs)#asks for user inputs
        prop_form = ['str','str','str','str']#error checking
        if self.iterate_check(inputs,prop_form) == False:return#is this is true it means user returned to dashboard
        regno = UniqueIDManager.getUniqueRegistrationNumber('marriages')#generate unique number
        regdate = self.get_current_date()
        regplace = User.getUserCity()#get the city of the loged in user
        if self.check_person(inputs['partner1_fname'],inputs['partner1_lname']):#True if partner_1 is not in database
            print(f"Enter the following information about {inputs['partner1_fname']} {inputs['partner1_lname']}")
            columns2 = {'bdate': None,'bplace': None,'address': None,'phone': None}
            columns2 = self.iterate(columns2)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if self.iterate_check(columns2,prop_form) == False:return#is this is true it means user returned to dashboard
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{inputs['partner1_fname']}','{inputs['partner1_lname']}','{columns2['bdate']}','{columns2['bplace']}','{columns2['address']}','{columns2['phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print(f"error when inserting {inputs['partner1_fname']} {inputs['partner1_lname']}")
        if self.check_person(inputs['partner2_fname'],inputs['partner2_lname']):#True if partner2 is not in database
            print(f"Enter the following information about {inputs['partner2_fname']} {inputs['partner2_lname']}")
            columns3 = {'bdate': None,'bplace': None,'address': None,'phone': None}
            columns3 = self.iterate(columns3)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if self.iterate_check(columns3,prop_form) == False:return#is this is true it means user returned to dashboard
            try:
                cursor.execute(f'''INSERT INTO persons VALUES 
                ('{inputs['partner2_fname']}','{inputs['partner2_lname']}','{columns3['bdate']}','{columns3['bplace']}','{columns3['address']}','{columns3['phone']}');''')
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print(f"error when inserting data about {inputs['partner2_fname']} {inputs['partner2_lname']}")
        ##################################################################################
        # register marriage SQL logic goes here
        try:
            cursor.execute(f"INSERT INTO marriages VALUES ('{regno}','{regdate}','{regplace}','{inputs['partner1_fname']}','{inputs['partner1_lname']}','{inputs['partner2_fname']}','{inputs['partner2_lname']}')")
            sqlCursor.get_instance().get_connection().commit()
        except sqlCursor.get_error() as e:
            print("error when inserting marriage")
        # end logic
        ##################################################################################
        print("successfully registered marriage\n")
        SysCallManager.ReturnToDashboard()
        return
    def renewVehicleRegistration(self):
        '''
        This function renews mutates the vehicle registration of an existing vehicle on the database.
        It does not return anything
        '''
        # allow registry agent to renew their registration
        # perform issue ticket steps
        cursor = sqlCursor.get_instance().get_cursor()
        regno = input("Enter registry number: ")
        exist = not(self.reg_exist(regno))#
        while exist:# check if registraion num exist
            print('Registration not found')
            option = input("Enter (1) to enter a different registry number\nPress any other button  to return to dashboard: ")
            if option == '1':
                regno = input("Enter registry number: ")
                exist = not(self.reg_exist(regno))
            else:
                SysCallManager.ReturnToDashboard()
                return
        try:
            cursor.execute("SELECT expiry FROM registrations WHERE regno=?;",regno)
        except sqlCursor.get_error() as e:
            print(f"error when retrieving data about vehicle with vin number: {regno}")
        cur_expiry = cursor.fetchone()[0]
        try:
            cursor.execute(f"SELECT strftime('%s','now') - strftime('%s',:cur_expiry);",{'cur_expiry':cur_expiry})#calculating time difference in unix timestamp
        except sqlCursor.get_error() as e:
            print(f"error when retrieving data about date {cur_expity}")
        ##################################################################################
        # renew vehicle registration SQL logic goes here
        if cursor.fetchone()[0] < 0:#registration is not expired
            new_date = str(int(cur_expiry[:4])+1)+(cur_expiry[4:])
            #slef.get_current_date returns an integer so need to convert it to a string to concatenate
            #will concatante first 4 letters of the string, which is the year, turn it into an integer add1 to it and then
            #turn it back to a string and concatinate it back to the rest of the dates.
            try:
                cursor.execute("UPDATE registrations SET expiry=:new_date WHERE regno=:regno;",{'new_date':new_date,'regno':regno})
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print(f"error when updating {new_date } and {regno}")
        else:#registration is expired
            cur_date = self.get_current_date()
            new_date = str(int(str(cur_date)[:4])+1)+(cur_date[4:])
            #will concatante first 4 letters of the string, which is the year, turn it into an integer add1 to it and then
            #turn it back to a string and concatinate it back to the rest of the dates.
            try:
                cursor.execute("UPDATE registrations SET expiry=:new_date WHERE regno=:regno;",{'new_date':new_date,'regno':regno})
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print(f"error when updating {new_date} and {regno}")
        # end logic
        ##################################################################################
        print("successfully renewed vehicle registration\n")
        SysCallManager.ReturnToDashboard()
        return
    def processBillOfSale(self):
        '''
        This Functions inserts values into the registration table in the database. Some of the inserted values
        are inputed by the user and some are generated by the database. This function does not return anything.
        '''
        cursor = sqlCursor.get_instance().get_cursor()
        # allow rgistry agent to process a bill of sale
        # perform issue ticket steps
        inputs = {'vin_of_car':None,'firstname_of_current_owner':None,\
            'lastname_of_current_owner':None,'firstname_of_new_owner':None,\
                'lastname_of_new_owner':None,'New_plate_number':None}
        inputs = self.iterate(inputs)#asks for user inputs
        prop_form = ['None','str','str','str','str','None']#error checking, vin and platenumber can be anything
        if self.iterate_check(inputs,prop_form) == False:return#is this is true it means user returned to dashboard
        try:
            cursor.execute(f"SELECT fname,lname FROM registrations WHERE vin=:vin ORDER BY regdate DESC;",{'vin':inputs['vin_of_car']})
        except sqlCursor.get_error() as e:
            print(f"error when retrieving data from vehicle with vin: {inputs['vin_of_car']}")
        owner = cursor.fetchone() 
        if owner == None or (owner[0] != inputs['firstname_of_current_owner'] or owner[1] != inputs['lastname_of_current_owner']):
            #This will check if the most recent owner of the vehicle is the inputed current owner and if it isnt user will be returned to Dashboard
            print(f"The inputed vehicle with the vin number {inputs['vin_of_car']} is not currently owned by {inputs['firstname_of_current_owner']} {inputs['lastname_of_current_owner']}")
            SysCallManager.ReturnToDashboard()
            return
        regno = UniqueIDManager.getUniqueRegistrationNumber('registrations')#generate unique number
        regdate = str(self.get_current_date())
        ##################################################################################
        # process bill of sale SQL logic goes here
        try:
            cursor.executescript(f'''UPDATE registrations SET expiry = '{self.get_current_date()}' WHERE vin = '{inputs['vin_of_car']}';
                                INSERT INTO registrations VALUES ('{regno}','{regdate}','{str(int(regdate[:4])+1)+regdate[4:]}',\
                                    '{inputs['New_plate_number']}','{inputs['vin_of_car']}','{inputs['firstname_of_new_owner']}',\
                                        '{inputs['lastname_of_new_owner']}');''')
            sqlCursor.get_instance().get_connection().commit()
        except sqlCursor.get_error() as e:
            print("error when proccessing bill of sale:" +  e)
        # end logic
        ##################################################################################
        print("successfully processed bill of sale\n")
        SysCallManager.ReturnToDashboard()
        return
    def processPayment(self):
        '''
        This function inserts values into the tickets table. The inserted values are generated by the user.
        Queries are used to check if the inputed payment is eligible to be inserted to the databse.
        '''
        cursor = sqlCursor.get_instance().get_cursor()
        # allow registry agent to process a payment
        # perform issue ticket steps
        tno = input("Enter ticket number: ").strip()
        while not(tno).isdigit(): tno = input("Ticket number must be a digit : ")
        cursor.execute(f"SELECT fine FROM tickets WHERE tno={tno};")
        fine = cursor.fetchone()
        if fine == None:#error check if ticket is valid
            print('Ticket does not exist')
            SysCallManager.ReturnToDashboard()
            return
        payment = int(input(f"Enter payment amount,payment required {fine[0]}: "))
        if payment <= 0:
            print('Payment must be greater than 0$')
            SysCallManager.ReturnToDashboard()
            return
        fine = fine[0]
        if payment > int(fine):#error check if the payment is bigger than the entire fine
            print('Payment exceeds fine')
            SysCallManager.ReturnToDashboard()
            return
        cursor.execute("SELECT strftime('%Y-%m-%d %H:%M:%S','now');")#this will give the current date withhours,minutes, and seconds
        cur_date = cursor.fetchone()[0]
        ##################################################################################
        # process payment SQL logic goes here
        cursor.execute(f"SELECT sum(amount) FROM payments WHERE tno=? GROUP BY tno;",tno)
        cur_payments = cursor.fetchone()
        if cur_payments == None:#True if no payments have been made yet
            try:
                cursor.execute(f"INSERT INTO payments VALUES ('{tno}','{cur_date}',{payment});")
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print(f"error when inserting ticket payment: {tno}")
        else:
            cur_payments = cur_payments[0]
            if (int(cur_payments) + payment) <= fine:
                try:
                    cursor.execute(f"INSERT INTO payments VALUES ('{tno}','{cur_date}',{payment});")
                    sqlCursor.get_instance().get_connection().commit()
                except sqlCursor.get_error() as e:
                    print(f"error when inserting ticket payment: {tno}")
            else:
                print('sum of payments exceeds fine')
                SysCallManager.ReturnToDashboard()
                return
        # end logic
        ##################################################################################
        print("successfully processed payment\n")
        SysCallManager.ReturnToDashboard()
        return
    def getDriverAbstract(self):
        '''
        This function will ask the user to input a first name and a last name. All queries are used to 
        retrive data from the database.
        '''
        cursor = sqlCursor.get_instance().get_cursor()
        fname = input('Enter first name: ').strip()
        lname = input('Enter last name: ').strip()
        ##################################################################################
        # get driver abstract SQL logic goes here
        if self.check_person(fname,lname):#will return true if the inputed person is not in the database
            print(f"{fname} {lname} is not in the database")
            SysCallManager.ReturnToDashboard()
            return
        try:
            cursor.execute(f'''
                        SELECT COUNT(*),sum(points) FROM demeritNotices d
                        WHERE d.fname =:fname AND d.lname =:lname;''',{'fname':fname,'lname':lname})
        except sqlCursor.get_error() as e:
            print(f"error when trying to retrieve informtion about {fname} {lname}")
        num_dnotice = cursor.fetchone()
        if num_dnotice[1] == None: num_dnotice = (num_dnotice[0],0)#change the sum of total demerit points to 0 from None if there are no demerit points
        try:
            cursor.execute(f'''
                        SELECT sum(points) FROM demeritNotices 
                        WHERE fname = :fname AND lname = :lname
                        AND  (julianday('now')-julianday(ddate)) <= 730;
                        ''',{'fname':fname,'lname':lname})
        except sqlCursor.get_error() as e:
            print(f"error when retrieving data about {fname} {lname}")
        num_points = cursor.fetchone()
        if num_points[0] == None: num_points = 0#change the sum of total demerit points to 0 from None if there are no demerit points
        else: num_points = num_points[0]
        try:
            cursor.execute(f'''SELECT t.tno,t.vdate,t.violation,t.fine,r.regno,v.make,v.model FROM tickets t,registrations r,vehicles v 
                        WHERE r.fname =:fname AND r.lname =:lname AND r.regno = t.regno
                        AND r.vin = v.vin ORDER BY t.vdate DESC;''',{'fname':fname,'lname':lname})
        except sqlCursor.get_error() as e:
            print(f"error when retrieving data about {fname} {lname}")
        tickets = cursor.fetchall()
        if tickets == None:tickets=0
        print(f"-----{fname} {lname}'s Driver Abstract-----\nnumber of tickets: {len(tickets)}\nnumber of demerit notices: {num_dnotice[0]}\nnumber of demeritpoints within the past 2 years: {num_points}\ntotal number of demerit points: {num_dnotice[1]}")
        option = input(f"view {fname} {lname}'s tickets (Y/N)?: ")
        start = 0
        end = 0
        if len(tickets) >= 5:
            end = 5
        else:
            end = len(tickets)
        while option.lower() != 'n':
            for item in range(start,end):
                print(f"\n\nticket number: {tickets[item][0]}\nticket date: {tickets[item][1]}\nticket description: {tickets[item][2]}\nticket fine: {tickets[item][3]}\nvehicle registration:{tickets[item][4]}\nvehicle make: {tickets[item][5]}\nvehicle model: {tickets[item][6]}")
                if item == len(tickets)-1:#at the last ticket
                    option = 'n'
                    break
            if option == 'n':break
            option = input('View more tickets (Y/N): ')
            start = end
            end += 5
        print()
        # end logic
        ##################################################################################
        print("successfully retrieved driver abstract\n")
        SysCallManager.ReturnToDashboard()
        return