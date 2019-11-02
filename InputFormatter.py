from SysCallManager import SysCallManager

class InputFormatter:
    @staticmethod
    def formatToCaseSensitiveLower(inputString):
        # convert string to lower case format
        if (isinstance(inputString, str)):
            return inputString.lower()
        else:
            return None

    @staticmethod
    def formatToCaseSensitiveUpper(inputString):
        # convert string to upper case format
        if (isinstance(inputString, str)):
            return inputString.upper()
        else:
            return None

    @staticmethod
    def ensureValidInput(inputMessage, validResponses):
        # returned response deos not neccesarily
        Exit = False
        while (not Exit):
            response = input(inputMessage)
            for r in validResponses:
                if (r == response):
                    Exit = True
            
        return response
        
    @staticmethod
    def iterate(dict,keys):#created to eliminate redundancy 
        #only dictionaries should be passed to this function.
        #returns a mutated dictionary object
        for item in keys:
            dict[item] = input('Enter {}: '.format(item))
        return dict
    @staticmethod
    def is_string(inp):#checks if input is string
        #returns a boolean value dpending on the format of the string.
        if inp == '' or inp == None:return False#cant be null
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
            if InputFormatter.date_form(inp):return True
            return False
        elif len(inp) == 19:#date might include the seconds and hour hence its of the form 'YYYY-MM-DD HH:MM:SS'
            inp = inp.strip()#take out all the spaces
            if InputFormatter.date_form(inp):#will return True if the first 10 characters of date is correct
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
            if InputFormatter.re_input(cont,attr) == False:
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
        option = input("{} has an incorrect format. Press 'Y' to re-enter a new {} or 'N' to return to dashboard: ".format(attr,attr).strip())
        while option.lower() != 'n': 
            if option.lower() == 'y':
                cont[attr] = input("Enter new {}: ".format(attr).strip())
                return
            option = input("{} has an incorrect format. Press 'Y' to re-enter a new {} or 'N' to return to dashboard: ".format(attr,attr).strip())
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
    def iterate_check(inp,prop_form,keys):
        '''
        inp: is the dictionary object containing inputs from the user
        prop_form: is a list object containing what formats should be inserted to sqlite
        keys: list of dictionary keys which are columns

        This function does not return anything.Rather it mutates the inp object by calling other functions.
        '''
        for item in range(0,len(inp)):#inp and prop_form are indexed so that the 
            #index of the 'proper format' in prop_form corresponds to the proper format of
            #the user's input contained in 'inp'.
            if prop_form[item] == 'str':
                if InputFormatter.inp_check(inp,keys[item],InputFormatter.is_string) == False:return False
            elif prop_form[item] == 'phone':
                if InputFormatter.inp_check(inp,keys[item],InputFormatter.is_phone) == False:return False
            elif prop_form[item] == 'date':
                if InputFormatter.inp_check(inp,keys[item],InputFormatter.is_date) == False:return False