min_lenght = 21;

while True:
    name =input("please Enter your name: ");
    if len(name) >= min_lenght and name.isalpha() and name.isprintable():
        break
    else:
        print("błąd");