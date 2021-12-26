# imports
import termcolor

passwords_tried = [] # list to store all failed passwords
password = ''
count = 0 # keeps track of how many failed attempts
print("Enter Password")

# The password is admin
while password != "admin": # if password is incorrect
    password = input()
    count += 1
    if password == "admin": # if password is correct
        for Password in passwords_tried:
            print(Password)
        
        print(termcolor.colored(("[++]Password Correct"), 'green', attrs=['blink', 'bold']))
    else:
        passwords_tried.append(password + " --> " + str(count))