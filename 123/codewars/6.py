# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!
# if is on the list = ["Mr Spock","Captain Kirk","Dr. McCoy","Liutenant Uhura"]
# Example output:
# Hello, Mr. Spock

def say_hello(name):
    crew = ["Mr Spock","Captain Kirk","Dr. McCoy","Liutenant Uhura"]
    if name in crew:
        return f"Hello, {name}"
    else:
        return "Error"

print(say_hello("Mr King"))
print(say_hello("Mr Spock"))