from datetime import date 

import socket 
class Assignment2: 
    
    def __init__(self, birthYear):
        self.birthYear = birthYear
    
    def tellAge(self, year):
        print(f"Your age is {self.birthYear - year}")
    
    def listAnniversaries(self) -> list: 
        num_aniversaries = (self.birthYear - date.today().year) // 10
        aniversaries = []
        for x in range(1,num_aniversaries):
            aniversaries.append((x * 10))
        return aniversaries
    
    def modifyYear(self, number) -> str:
        string_ver = f'{self.birthYear}'[0:2] * n
        odd_chars = ""
        for x in range(0, n, step=2):
            odd_chars = odd_chars + self.birthYear[x]
        return string_ver + odd_chars
    
    @staticmethod
    def checkGoodString(string: str) -> bool: 
        is_good_len = len(string) >= 9
        is_good_start_char = string[0] in range(ord('a'), ord('z'))
        contains_only_one_numer = False
        for character in string:
            if character.isdigit() and not contains_only_one_numer:
                contains_only_one_numer = True
            if character.isdigit() and contains_only_one_numer:
                contains_only_one_numer = False
                break
        return (is_good_len and is_good_start_char and contains_only_one_numer)
    
    @staticmethod
    def connectTo(url: str, port: int ) -> bool :
        HOST = "127.0.0.1"
        PORT = 65432
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            host_ip = socket.gethostbyname(url)
            s.connect((host_ip, port))
            try:
                s.send("test")
                return True
            except:
                return False