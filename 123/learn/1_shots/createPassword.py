import random
# Define character
letters_numbers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
                   'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
                    '0','1','2','3','4','5','6','7','8','9']
special_characters = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', '-', '^', '~', '+', '/', '=', '<', '>', '?', '\'', 
                      '\"', ',', '.',]

#Generate a random password

def generate_password():
    password_length = random.randint(2, 5)
    password = []
    for i in range(password_length):
        password.append(random.choice(letters_numbers))
        password.append(random.choice(special_characters))

    return ''.join(password)
print("\n\n")
how_many_passwords = 10
while how_many_passwords >= 0:
    print(generate_password())
    how_many_passwords -= 1