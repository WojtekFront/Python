# class: 
# ask for file
# checke file exists
# check format is JSON
# show tree in file
import json
import os
import sys


class Open_csv:


    os.chdir(r'C:\Pyt\Python\app\examples')
            

    def __init__(self, filepath ):
        self.filepath = filepath
        self.file_object = None
        self.file_json = False


    def open_file(self):
        try:
            with open(self.filepath, 'r') as file_object:
                print("File exists")
                self.file_object= file_object
                self.check_json()
        except FileNotFoundError:
            print("Error: File not found")
            exit()
        
        
    def check_json(self):
        try:
            self.file_object.seek(0)
            json.load(self.file_object)
            self.file_json = True
            print("File is in JSON format")
        except json.JSONDecodeError as e:
            print("Error:check_json {0}".format(e))
            self.file_json = False
        except Exception as e:
            print(f"An error occurred: {e}")

    



new_file = Open_csv("product1.json")

new_file.open_file()   


