import os
import datetime

os.chdir(r'C:\Pyt\Python\work_with_python\0_text_append')

def create_file_name(): 
    return datetime.datetime.now().strftime('%y-%m-%d') + ".txt"

# open the file
try:
    new_text = open(create_file_name(), 'x')
except:
    new_text = open(create_file_name(), 'r+')


new_text.write("This is new Python line " + datetime.datetime.now().strftime('%H:%M:%S') + "\n")
if new_text:
    for line_x in new_text:
        print(line_x)
else:
    print("We don't have anything")


# close the file
new_text.close()