long_text = "1234567890"
new_text = ""
for index in range(len(long_text)):
    if index % 2 == 1:
        print(long_text[index])
        new_text += long_text[index]
print(new_text)