import termcolor

passwords_tried = []
password = ''
count = 0
print("Enter Password")

while password != "admin":
    password = input()
    count += 1
    if password == "admin":
        for Password in passwords_tried:
            print(Password)
        
        print(termcolor.colored(("[++]Password Correct"), 'green', attrs=['blink', 'bold']))
    else:
        passwords_tried.append(password + " --> " + str(count))