# class: 
# ask for file
# checke file exists
# check format is JSON
# show tree in file
import json
import os
import sys
import datetime
import string

os.chdir(r'C:\Pyt\Python\app\1_json\examples')
class Error_message:
    def __init__(self, error_message = ""):
        self.error_message = error_message
        self.log_path = "../backup/log.txt"

    def  collect_errors_message(self):
        write_error_message = open(self.log_path, 'w')
        write_error_message.write(self.error_message)
        write_error_message.close()

class Open_csv(Error_message):
    '''The Open_csv class opens a file and checks whether it exists and its format. If it exists, it creates a copy of it in the backup that 
    you can work on (date_time_name start).'''

    # os.chdir(r'C:\Pyt\Python\app\1_json\examples')

    def __init__(self, filepath, error_message=""):
        self.filepath = filepath # self.filepath - path to the file
        self.file_object = None # self.file_object - 
        self.file_json = False
        self.new_text_json = None
        self.backup_name_file = "" # after import you can working on this file
        super().__init__(error_message)

    def open_file(self):
        '''open file for reading'''
        try:
            with open(self.filepath, 'r') as file_object:
                self.file_object= file_object
                self.check_json() # go to function
        except FileNotFoundError:
            print("Error: File not found")
            sys.exit(0)
        
    def check_json(self):
        '''check it is a json formatted file'''
        try:
            self.file_object.seek(0)
            self.new_text_json= json.load(self.file_object)
            self.file_json = True
            self.create_backup_name_file()
        except json.JSONDecodeError as e:
            print("Error:check_json {0}".format(e))
            self.file_json = False
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(0)

    def create_backup_name_file(self):
        '''Create a new file and open import file'''
        # create name for file
        copy_count = 11 # hom many sign after date
        for sign in self.filepath:
            copy_count -= 1
            if (sign == ".") or (copy_count <= 0):
                self.connect_backup_name()
                self.create_backup_file()
                sys.exit(0)
            # elif sign == " ":
            #     self.backup_name_file += "_"
            elif sign in set(string.ascii_letters + string.digits):
                self.backup_name_file += sign
            else:
                self.backup_name_file += "_"

    def connect_backup_name(self):
        self.backup_name_file = datetime.datetime.now().strftime("%y%m%d_%H%M%S_") + self.backup_name_file + ".txt"

    def create_backup_file(self):

        # !!! temporay name !!!
        self.backup_name_file = "temporary.txt"
        new_backup_file = open(self.backup_name_file,"w")
        
        # !!! correct name !!!
        # new_backup_file = open(self.backup_name_file,"x")
        
        new_backup_file.write(str(self.new_text_json))
        new_backup_file.close()

    def test_analyze_json(self):
        print("open")
        data= self.new_text_json
        if isinstance(data, list): 
            data = data[0]

        print("Pola i ich format w pliku JSON")
        for key, value in data.items():
            print(f"{key}: {type(value).__name__}")



try:
    input_values = "person1.json"
except:
    print("Please select correct input file ")
    sys.exit(0)

new_file = Open_csv(input_values)


new_file.open_file()   
new_file.test_analyze_json()
# new_file.collect_errors_message()


