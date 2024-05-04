#import libraries
import random
from cryptography.fernet import Fernet

#generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)


class memorable:
    def __init__(self, memorable_word, lstIndex, lstLetter):
        self.memorable_word = memorable_word
        self.lstIndex = []
        self.lstLetter = []
        
    def Memory(self):
        lstItem = enumerate(self.memorable_word, start=1)
        lstItemSelected = random.sample(list(lstItem), 3)
        self.lstIndex = [index[0] for index in lstItemSelected]
        self.lstLetter = [letter[1] for letter in lstItemSelected]
        return self.lstIndex, self.lstLetter
        
    def Encrypt(self):
        posLetterEncrypt = [cipher.encrypt(letter.encode()) for letter in self.lstLetter]
        return posLetterEncrypt
        
    def Decrypt(self):
        posLetterDecrypt = [cipher.decrypt(letter).decode() for letter in self.Encrypt()]
        return posLetterDecrypt
        