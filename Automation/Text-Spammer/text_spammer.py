# imports 
import pyautogui
import win32clipboard

# defining class
class spammer():
    # initating class
    def __init__(self, text="", count=1):
        self.count = count

        if text == "": # checking the value of text

            # copying the clipboard
            win32clipboard.OpenClipboard()
            self.text = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
        else:
            self.text = text

    def Paste(self):
        count = int(self.count)
        while count != 0:
            text = str(self.text)
            pyautogui.typewrite(text)
            pyautogui.press('enter')
            count -= 1

if "__main__" == __name__:
    text = input("Enter Text To Paste "
    "(If Empty Will Paste ClipBoard): ")
    count = input("How Many Times To Paste: ")

    bot = spammer(text, count)
    bot.Paste()