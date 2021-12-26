import pyautogui
import sys, os
import termcolor


class spammer():
    def __init__(self, path="C:\\Users\\mayan\\Desktop\\Programing\\Python\\Python-Macro-Apps\\Text-Spammer\\file.txt"):

        if os.path.exists(path):
            self.path = path
        else:
            print(termcolor.colored(("FILE/PATH INVALID"), 'red'))
            sys.exit(0)

    def Paste(self):
        file = open(self.path, 'r')
        for line in file:
            pyautogui.typewrite(line)

if "__main__" == __name__:

    bot = spammer()
    bot.Paste()