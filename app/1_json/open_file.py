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

class Open_csv:


    os.chdir(r'C:\Pyt\Python\app\examples')
            

    def __init__(self, filepath ):
        self.filepath = filepath
        self.file_object = None
        self.file_json = False
        self.new_text_json = None
        self.backup_name_file = "" # 

    def open_file(self):
        try:
            with open(self.filepath, 'r') as file_object:
                print("File exists")
                self.file_object= file_object
                self.check_json()
        except FileNotFoundError:
            print("Error: File not found")
            sys.exit(0)
        
    def check_json(self):
        try:
            self.file_object.seek(0)
            self.new_text_json= json.load(self.file_object)
            self.file_json = True
            self.copy_text()

        except json.JSONDecodeError as e:
            print("Error:check_json {0}".format(e))
            self.file_json = False
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(0)

    def copy_text(self):
        # create neme for file
        copy_count=0
        for sign in self.filepath:
            copy_count += 1
            if (sign == ".") or (copy_count >= 11):
                self.generatename()
                sys.exit(0)
            elif sign == " ":
                self.backup_name_file += "_"
            elif sign in set(string.ascii_letters + string.digits):
                self.backup_name_file += sign
            else:
                self.backup_name_file += "_"
                
        return self.backup_name_file

    def generatename(self):
        # create a new file with current date name
        # print(self.backup_name_file)
        self.backup_name_file = datetime.datetime.now().strftime("%y%m%d_%H%M%S_") + self.backup_name_file + ".txt"
        print(self.backup_name_file )
        # copies contents of the file 

    
        # print(self.new_text_json)
        # print("File is in JSON format")

new_file = Open_csv("person1.json")
# new_file = Open_csv("person2.json")

new_file.open_file()   


