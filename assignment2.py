import socket
import sys


class Assignment2:
    def __init__(self, year):
        self.year = year
        
    def tellAge(self, currentYear):
        print("Your age is " + str(currentYear - self.year))
    
    def listAnniversaries(self):
        currentYear = 2022
        test = currentYear - self.year
        a = []
        if test > 2:
            a = [10]
        else:
            a = [10, 20]
        return a

    def modifyYear(self, n):
        ans = str(self.year)[:2] * n
        s = self.year * n
        ans = ans + str(s)[::2]
        return ans

    def checkGoodString(string:str):
        if len(string) < 9:
            return False
        
        if string[0].islower() == False:
            return False
        
        digitCounter = 0
        for i in string:
            if i.isdigit():
                digitCounter += 1
            
            if digitCounter > 1:
                return False
        
        return True

    def connectTcp(AF_INET, SOCK_STREAM):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverAddress = (AF_INET, int(SOCK_STREAM))
        print("Connecting to %s on port %s " % serverAddress)

        try:
            hostIP = socket.gethostbyname(AF_INET)
        except socket.gaierror:
            return False
        try:
            s.connect(serverAddress)
            return True
        except socket.error:
            return False

a = Assignment2(2000)
ret = a.listAnniversaries()
print(ret)