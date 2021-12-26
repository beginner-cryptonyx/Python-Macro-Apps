# imports
import win32clipboard
from random import randint

class PasswordGenerator():

    # initialize the class
    def __init__(self):
        pass
    
    # Password Generator
    def Generate(self, digits:float, isCopy:bool=False) -> str:

        # varables of the char in ascii
        numbers = '1234567890'
        letters_lowered = u'abcdefghijklmnopqrstuvwxyz'
        letters_uppered = letters_lowered.upper()
        symbols = u'!@#$%^&*()-=+~`:;|\{}_,<.>/'
        TotalChars = list(letters_lowered + letters_uppered + letters_uppered + symbols)

        passwordList = []
        
        for _ in range(0, digits):
            passwordList.append(TotalChars[randint(0, len(TotalChars)-1)])
        
        password = ''
        for item in passwordList:
            password += str(item)

        if isCopy == True:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(password)
            win32clipboard.CloseClipboard()

            
        return str(password).strip('[').strip(']').strip("'")


if __name__ == '__main__':
    bot = PasswordGenerator()
    print(bot.Generate(16, isCopy=True))