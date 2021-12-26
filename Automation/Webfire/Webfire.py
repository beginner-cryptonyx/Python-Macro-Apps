# Imports
import webbrowser as web
import subprocess, re, sys

# defining the class
class WebFire():

    #initiating the class
    def __init__(self):
        pass

    def open(self, website):
        web.open(website, 2)
    
    def Fire(self) -> bool:
        with open('WebFire/websites.txt', 'r') as file:
            for website in file:
                self.open(website)
                return True
    
    def checkState(self, website):
        result = subprocess.run(['ping', str(website)], capture_output=True)
        filter = re.findall('Reply from', str(result))
        
        if 'Reply from' in filter:
            return True

        else: 
            return False

    def checkIP(self, website):
        result = subprocess.run(['tracert', website])
        print(result)
        
        
        
        

if __name__ == '__main__':
    bot = WebFire()
    bot.checkIP('www.testphp.vulnweb.com')
    # bot.checkState('www.google.com')
    # if bot.checkState('www.facebook.com') == True:
    #     print('true')