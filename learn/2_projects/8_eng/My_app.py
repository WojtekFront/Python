import json
import os
os.chdir(r'C:\Pyt\Python\sup')

try:
    text_to_read = open(os.path.join(os.getcwd(),"csv","english1.csv"), "r")
    print(text_to_read.read())
    text_to_read.close()
except Exception as e:
    print("Cannot open", e)
    # print("Couldn't open{0}".format(text_to_read))


# class My_app:
    
#     def __init__(self, new_file):
#         self.new_file = new_file
#         self.file = open(self.new_file, "r")
    
#     def read_file(self):
#         return self.file.read()
    

# path_english_file = "csv/engilsh1.csv"
# app = My_app(path_english_file)
              
# file_contet = app.read_file()
# print(file_contet)
# print("ffff")
