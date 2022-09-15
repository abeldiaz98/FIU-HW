import socket
import sys


class Assignment2:
    def __init__(self, year):
        self.year = year
        
    def tellAge(self, currentYear):
        print("Your age is " + str(currentYear - self.year))
    
    def listAnniversaries(self):
        temp = 10
        year = 2022
        year = year - year % 10
        a = []
        while (year > self.year):
            a.append(temp)
            year = year - 10
            temp = temp + 10

        return a

    def modifyYear(self, n):
        ans = str(self.year)[:2] * n
        s = self.year * n
        ans = ans + str(s)[::2]
        return ans

    def checkGoodString(string:str):
        if (len(string) < 9):
            return False
        else:
            if (string[0].islower() and any(c.isdigit() for c in string)):
                return True
            else:
                return False

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

ret = Assignment2.checkGoodString("a1aaaaaa")
print(ret)