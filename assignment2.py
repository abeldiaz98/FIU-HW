import socket
import sys
from re import A


class Assignment2:
    def __init__(self, year):
        self.year = year
        
    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is %d", age)
    
    def listAnniversaries(self):
        a = Assignment2(2022)
        ret = a.listAnniversaries()
        return ret

    def modifyYear(self, n):
        num = n
        res = ""
        arr = str(num)
        for i in range(n):
            res += arr[:2]
        num = num*n
        lst = str(num)
        arr1 = lst[::2]
        res += arr1
        return res

    def checkGoodString(string):
        if len(string) < 9:
            return False
        
        if string[0].islower() == False:
            return False
        
        _num_count = 0
        for i in string:
            if i.isdigit():
                _num_count += 1
            
            if _num_count > 1:
                return False
        
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
   
