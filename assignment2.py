from datetime import date 

import socket 
class Assignment2: 
    def __init__(self, year):
        self.year = year
    
    def tellAge(self, currentYear: int):
        print(f"Your age is {currentYear - self.year}")
    
    def listAnniversaries(self) -> list: 
        num_aniversaries = (date.today().year - self.year ) // 10
        aniversaries = []
        for x in range(1,num_aniversaries + 1):
            aniversaries.append((x * 10))
        return aniversaries
    
    def modifyYear(self, n: int) -> str:
        str_year = f'{self.year}'
        string_ver = str_year[0:2] * n
        odd_chars = ""
        for x in range(0, n, 2):
            try:
                odd_chars = odd_chars + str_year[x]
            except:
                break
        return string_ver + odd_chars
    
    @staticmethod
    def checkGoodString(string: str) -> bool: 
        is_good_len = len(string) >= 9
        a: int = ord('a')
        z: int = ord('z')
        is_good_start_char = ord(string[0]) <= z and ord(string[0]) >= a
        contains_only_one_numer = False
        for character in string:
            if character.isdigit() and not contains_only_one_numer:
                contains_only_one_numer = True
            elif character.isdigit() and contains_only_one_numer:
                contains_only_one_numer = False
                break
        return (is_good_len and is_good_start_char and contains_only_one_numer)
    
    @staticmethod
    def connectTcp(host: str, port: int ) -> bool :
        HOST = "127.0.0.1"
        PORT = 65432
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            host_ip = socket.gethostbyname(host)
            try:
                s.connect((host_ip, port))
                s.close()
                return True
            except:
                s.close()
                return False
            
if __name__ == "__main__":
    a = Assignment2(2000)
    ret = a.modifyYear(5)
    print(ret)
    ret = Assignment2.checkGoodString("f1obar0more")
    print(ret)
    ret = Assignment2.checkGoodString("foobar0more")
    print(ret)
    retval = Assignment2.connectTcp("www.google.com", 80)
    print(retval)