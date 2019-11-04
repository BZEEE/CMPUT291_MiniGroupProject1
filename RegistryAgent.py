
from User import User
from SysCallManager import SysCallManager
from cursor import sqlCursor
from UniqueIDManager import UniqueIDManager
from InputFormatter import InputFormatter

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
    #================================================================================
    #THE FOLLOWING ARE HELPER FUNCTIONS
    @staticmethod
    def iterate(dict,keys):#created to eliminate redundancy 
        #only dictionaries should be passed to this function.
        #returns a mutated dictionary object
        for item in keys:
            dict[item] = input('Enter {}: '.format(item)).strip()
        return dict
    def check_person(self,p_fname,p_lname):#helper function for registerBirth
        #queries to check if the person is in the database.
        #return a boolean dpending on the pressence of 'p_fname' 'p_lname' in the database
        cursor = sqlCursor.get_instance().get_cursor()
        cursor.execute("SELECT fname,lname FROM persons WHERE fname=:p_fname COLLATE NOCASE AND lname=:p_lname COLLATE NOCASE;",{"p_fname":p_fname,"p_lname":p_lname})
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
        keys = ['fname','lname','gender','f_fname','f_lname','m_fname','m_lname','bdate','bplace']#needed to input user in proper order since dictionaries are not ordered
        columns = self.iterate(columns,keys)#asks for user inputs
        prop_form = ['str','str','str','str','str','str','str','date','str']#error checking
        if InputFormatter.iterate_check(columns,prop_form,keys) == False:return#if this is true it means user returned to dashboard
        if not(self.check_person(columns['fname'],columns['lname'])):#True if person is in the database
            print("{} {} is already in the database".format(columns['fname'],columns['lname']))
            return
        if self.check_person(columns['f_fname'],columns['f_lname']):#True if father is not in database
            print("Enter information about {} {}'s father'".format(columns['fname'],columns['lname']))
            columns2 = {'f_bdate': None,'f_bplace': None,'f_address': None,'f_phone': None}
            keys2 = ['f_bdate','f_bplace','f_address','f_phone']#needed to input user in proper order since dictionaries are not ordered
            columns2 = self.iterate(columns2,keys2)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if InputFormatter.iterate_check(columns2,prop_form,keys2,"null") == False:return#is this is true it means user returned to dashboard
            try:
                cursor.execute('''INSERT INTO persons VALUES 
                ('{}','{}','{}','{}','{}','{}');'''\
                    .format(columns['f_fname'],columns['f_lname'],columns2['f_bdate'],columns2['f_bplace'],columns2['f_address'],columns2['f_phone']))
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print("error when inserting details of {} {} into the database".format(columns['f_fname'],columns['f_lname']))
                return
        if self.check_person(columns['m_fname'],columns['m_lname']):#True if mother is not in database
            print("Enter information about {} {}'s mother'".format(columns['fname'],columns['lname']))
            columns3 = {'m_bdate': None,'m_bplace': None,'m_address': None,'m_phone': None}
            keys3 = ['m_bdate','m_bplace','m_address','m_phone']#needed to input user in proper order since dictionaries are not ordered
            columns3 = self.iterate(columns3,keys3)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if InputFormatter.iterate_check(columns3,prop_form,keys3,"null") == False:return#if this is true it means user returned to dashboard
            try:
                cursor.execute('''INSERT INTO persons VALUES 
                ('{}','{}','{}','{}','{}','{}');'''\
                    .format(columns['m_fname'],columns['m_lname'],columns3['m_bdate'],columns3['m_bplace'],columns3['m_address'],columns3['m_phone']))
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                    print("error when inserting details of {} {} into the database".format(columns['m_fname'],columns['m_lname']))
                    return
        regno = UniqueIDManager.getUniqueRegistrationNumber('births')#generate unique number
        regdate = self.get_current_date()
        regplace = User.getUserCity()#get the city of the loged in user
        #getting the mothers phone and address
        try:
            cursor.execute("SELECT address,phone FROM persons WHERE fname=:m_fname COLLATE NOCASE AND lname=:m_lname COLLATE NOCASE;",\
            {'m_fname':columns['m_fname'],'m_lname':columns['m_lname']})
        except sqlCursor.get_error() as e:
            print("error when retrieving data about {} {} ".format(columns['m_fname'],columns['m_lname']))
            return
        m_info = cursor.fetchone()
        m_address = m_info[0]#mothers address
        m_phone = m_info[1]#mothers phone number
        ##################################################################################
        # register birt SQL logic goes here
        try:
            cursor.executescript('''INSERT INTO births VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');
            INSERT INTO persons VALUES ('{}','{}' ,'{}' ,'{}','{}','{}');'''\
                .format(regno,columns['fname'],columns['lname'],regdate,regplace,columns['gender'],columns['f_fname'],columns['f_lname'],columns['m_fname'],columns['m_lname'],columns['fname'],columns['lname'],columns['bdate'],columns['bplace'],m_address,m_phone))
            sqlCursor.get_instance().get_connection().commit()
        except sqlCursor.get_error() as e:
            print("error when inserting details of {} {} into the database".format(columns['fname'],columns['lname']))
            return
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
        keys = ['partner1_fname','partner1_lname','partner2_fname','partner2_lname']
        inputs = self.iterate(inputs,keys)#asks for user inputs
        prop_form = ['str','str','str','str']#error checking
        if InputFormatter.iterate_check(inputs,prop_form,keys) == False:return#is this is true it means user returned to dashboard
        regno = UniqueIDManager.getUniqueRegistrationNumber('marriages')#generate unique number
        regdate = self.get_current_date()
        regplace = User.getUserCity()#get the city of the loged in user
        if self.check_person(inputs['partner1_fname'],inputs['partner1_lname']):#True if partner_1 is not in database
            print("Enter the following information about {} {}".format(inputs['partner1_fname'],inputs['partner1_lname']))
            columns2 = {'bdate': None,'bplace': None,'address': None,'phone': None}
            keys2 = ['bdate','bplace','address','phone']
            columns2 = self.iterate(columns2,keys2)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if InputFormatter.iterate_check(columns2,prop_form,keys2,"null") == False:return#if this is true it means user returned to dashboard
            try:
                cursor.execute('''INSERT INTO persons VALUES 
                ('{}','{}','{}','{}','{}','{}');'''.format\
                    (inputs['partner1_fname'],inputs['partner1_lname'],columns2['bdate'],columns2['bplace'],columns2['address'],columns2['phone']))
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print("error when inserting {} {}".format(inputs['partner1_fname'],inputs['partner1_lname']))
                return
        if self.check_person(inputs['partner2_fname'],inputs['partner2_lname']):#True if partner2 is not in database
            print("Enter the following information about {} {}".format(inputs['partner2_fname'],inputs['partner2_lname']))
            columns3 = {'bdate': None,'bplace': None,'address': None,'phone': None}
            keys3 = ['bdate','bplace','address','phone']
            columns3 = self.iterate(columns3,keys3)#asks for user inputs
            prop_form = ['date','str','None','phone']#error checking
            if InputFormatter.iterate_check(columns3,prop_form,keys3,"null") == False:return#if this is true it means user returned to dashboard
            try:
                cursor.execute('''INSERT INTO persons VALUES 
                ('{}','{}','{}','{}','{}','{}');'''.\
                    format(inputs['partner2_fname'],inputs['partner2_lname'],columns3['bdate'],columns3['bplace'],columns3['address'],columns3['phone']))
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print("error when inserting data about {} {}".format(inputs['partner2_fname'],inputs['partner2_lname']))
                return
        ##################################################################################
        # register marriage SQL logic goes here
        try:
            cursor.execute("INSERT INTO marriages VALUES ('{}','{}','{}','{}','{}','{}','{}')".format\
                (regno,regdate,regplace,inputs['partner1_fname'],inputs['partner1_lname'],inputs['partner2_fname'],inputs['partner2_lname']))
            sqlCursor.get_instance().get_connection().commit()
        except sqlCursor.get_error() as e:
            print("error when inserting marriage")
            return
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
        regno = input("Enter registry number: ").strip()
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
            print("error when retrieving data about vehicle with vin number: {}".format(regno))
            return
        cur_expiry = cursor.fetchone()[0]
        try:
            cursor.execute("SELECT strftime('%s','now') - strftime('%s',:cur_expiry);",{'cur_expiry':cur_expiry})#calculating time difference in unix timestamp
        except sqlCursor.get_error() as e:
            print("error when retrieving data about date {}".format(cur_expiry))
            return
        ##################################################################################
        # renew vehicle registration SQL logic goes here
        if cursor.fetchone()[0] < 0:#registration is not expired
            new_date = str(int(cur_expiry[:4])+1)+(cur_expiry[4:])
            #slef.get_current_date returns an integer so need to convert it to a string to concatenate
            #will concatante first 4 letters of the string, which is thhe year, turn it into an integer add1 to it and then
            #turn it back to a string and concatinate it back to the rest of the dates.
            try:
                cursor.execute("UPDATE registrations SET expiry=:new_date WHERE regno=:regno;",{'new_date':new_date,'regno':regno})
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print("error when updating {} and {}".format(new_date,regno))
                return
        else:#registration is expired
            cur_date = self.get_current_date()
            new_date = str(int(str(cur_date)[:4])+1)+(cur_date[4:])
            #will concatante first 4 letters of the string, which is the year, turn it into an integer add1 to it and then
            #turn it back to a string and concatinate it back to the rest of the dates.
            try:
                cursor.execute("UPDATE registrations SET expiry=:new_date WHERE regno=:regno;",{'new_date':new_date,'regno':regno})
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print("error when updating {} and {}".format(new_date,regno))
                return
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
        keys = ['vin_of_car','firstname_of_current_owner','lastname_of_current_owner','firstname_of_new_owner','lastname_of_new_owner','New_plate_number']
        inputs = self.iterate(inputs,keys)#asks for user inputs
        prop_form = ['None','str','str','str','str','None']#error checking, vin and platenumber can be anything
        if InputFormatter.iterate_check(inputs,prop_form,keys) == False:return#if this is true it means user returned to dashboard
        try:
            cursor.execute("SELECT fname,lname FROM registrations WHERE vin=:vin COLLATE NOCASE ORDER BY regdate DESC;",{'vin':inputs['vin_of_car']})
        except sqlCursor.get_error() as e:
            print("error when retrieving data from vehicle with vin: {}".format(inputs['vin_of_car']))
            return
        owner = cursor.fetchone() 
        if owner == None or (owner[0].lower() != inputs['firstname_of_current_owner'].lower() or owner[1].lower() != inputs['lastname_of_current_owner'].lower()):
            #This will check if the most recent owner of the vehicle is the inputed current owner and if it isnt user will be returned to Dashboard
            print("The inputed vehicle with the vin number {} is not currently owned by {} {}"\
                .format(inputs['vin_of_car'],inputs['firstname_of_current_owner'],inputs['lastname_of_current_owner']))
            SysCallManager.ReturnToDashboard()
            return
        regno = UniqueIDManager.getUniqueRegistrationNumber('registrations')#generate unique number
        regdate = str(self.get_current_date())
        ##################################################################################
        # process bill of sale SQL logic goes here
        try:
            cursor.executescript('''UPDATE registrations SET expiry = '{}' WHERE vin = '{}' COLLATE NOCASE;
                                INSERT INTO registrations VALUES ('{}','{}','{}','{}','{}','{}','{}');'''.format(self.get_current_date(),inputs['vin_of_car'],\
                                            regno,regdate,str(int(regdate[:4])+1)+regdate[4:],inputs['New_plate_number'],\
                                                inputs['vin_of_car'],inputs['firstname_of_new_owner'],inputs['lastname_of_new_owner']))
            sqlCursor.get_instance().get_connection().commit()
        except sqlCursor.get_error() as e:
            print("error when proccessing bill of sale")
            return
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
        try:#getting ticket fine
            cursor.execute("SELECT fine FROM tickets WHERE tno=?;",tno)
        except sqlCursor.get_error() as e:
            print("error when retrieving data about ticket with ticket number:{} ".format(tno))
            return
        fine = cursor.fetchone()
        try:#getting the sum of payments
            cursor.execute("SELECT sum(amount) FROM payments WHERE tno=? GROUP BY tno;",tno)
        except sqlCursor.get_error() as e:
            print("error when retrieving data about ticket with ticket number:{} ".format(tno))
            return
        cur_payments = cursor.fetchone()
        if fine == None:#error check if ticket is valid
            print('Ticket does not exist')
            SysCallManager.ReturnToDashboard()
            return
        if cur_payments == None:paid = 0
        else:paid = cur_payments[0]
        payment = int(input("Enter payment amount,payment required {}$: ".format(int(fine[0]) - int(paid)).strip()))
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
        if cur_payments == None:#True if no payments have been made yet
            try:
                cursor.execute("INSERT INTO payments VALUES ('{}','{}',{});".format(tno,cur_date,payment))
                sqlCursor.get_instance().get_connection().commit()
            except sqlCursor.get_error() as e:
                print("error when inserting ticket payment: {}".format(tno))
                return
        else:#payments have been made
            cur_payments = cur_payments[0]
            if (int(cur_payments) + payment) <= fine:
                try:
                    cursor.execute("INSERT INTO payments VALUES ('{}','{}',{});".format(tno,cur_date,payment))
                    sqlCursor.get_instance().get_connection().commit()
                except sqlCursor.get_error() as e:
                    print("error when inserting ticket payment: {}".format(tno))
                    return
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
            print("{} {} is not in the database".format(fname,lname))
            SysCallManager.ReturnToDashboard()
            return
        try:
            cursor.execute('''
                        SELECT COUNT(*),sum(points) FROM demeritNotices d
                        WHERE d.fname =:fname COLLATE NOCASE AND d.lname =:lname COLLATE NOCASE;''',{'fname':fname,'lname':lname})
        except sqlCursor.get_error() as e:
            print("error when trying to retrieve informtion about {} {}".format(fname,lname))
            return
        num_dnotice = cursor.fetchone()
        if num_dnotice[1] == None: num_dnotice = (num_dnotice[0],0)#change the sum of total demerit points to 0 from None if there are no demerit points
        try:
            cursor.execute('''
                        SELECT sum(points) FROM demeritNotices 
                        WHERE fname = :fname COLLATE NOCASE AND lname = :lname COLLATE NOCASE
                        AND  (julianday('now')-julianday(ddate)) <= 730 ;
                        ''',{'fname':fname,'lname':lname})
        except sqlCursor.get_error() as e:
            print("error when retrieving data about {} {}".format(fname,lname))
            return
        num_points = cursor.fetchone()
        if num_points[0] == None: num_points = 0#change the sum of total demerit points to 0 from None if there are no demerit points
        else: num_points = num_points[0]
        try:
            cursor.execute('''SELECT t.tno,t.vdate,t.violation,t.fine,r.regno,v.make,v.model FROM tickets t,registrations r,vehicles v 
                        WHERE r.fname =:fname COLLATE NOCASE AND r.lname =:lname COLLATE NOCASE AND r.regno = t.regno
                        AND r.vin = v.vin ORDER BY t.vdate DESC;''',{'fname':fname,'lname':lname})
        except sqlCursor.get_error() as e:
            print("error when retrieving data about {} {}".format(fname,lname))
            return
        tickets = cursor.fetchall()
        if tickets == None:tickets=0
        print("-----{} {}'s Driver Abstract-----\nnumber of tickets: {}\nnumber of demerit notices: {}\nnumber of demeritpoints within the past 2 years: {}\ntotal number of demerit points: {}"\
            .format(fname,lname,len(tickets),num_dnotice[0],num_points,num_dnotice[1]))
        option = input("view {} {}'s tickets (Y/N)?: ".format(fname,lname).strip())
        start = 0
        end = 0
        if len(tickets) >= 5:
            end = 5
        else:
            end = len(tickets)
        while option.lower() != 'n':
            for item in range(start,end):
                print("\n\nticket number: {}\nticket date: {}\nticket description: {}\nticket fine: {}\nvehicle registration:{}\nvehicle make: {}\nvehicle model: {}"\
                    .format(tickets[item][0],tickets[item][1],tickets[item][2],tickets[item][3],tickets[item][4],tickets[item][5],tickets[item][6]))
                if item == len(tickets)-1:#at the last ticket
                    option = 'n'
                    break
            if option == 'n':break
            option = input('View more tickets (Y/N): ').strip()
            start = end
            end += 5
        print()
        # end logic
        ##################################################################################
        print("successfully retrieved driver abstract\n")
        SysCallManager.ReturnToDashboard()
        return