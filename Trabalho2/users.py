"""
@author: Ian Zaniolo Sirbone
Title: Project 2
"""

from hashlib import sha256
from random import randint

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__role = self.__set_role(role)
        self.__rand_number = randint(0,100)
        self.__password_hash = self.__hash_password(password)

    #Getter do hash
    @property
    def password_hash(self) -> str:
        return self.__password_hash
    
    #Função de alterar senha
    def change_password(self, old_password, new_password) -> bool:
        if self.verify_password(old_password):
            self.__password_hash = self.__hash_password(new_password)
            return True
        else:
            return False
    
    #Função do hash com aleatoriedade
    def __hash_password(self, password):
        password = str(self.__rand_number)+password
        return sha256(password.encode('utf-8')).hexdigest()
    
    #Função de verificação de senha
    def verify_password(self, password) -> bool:
        if self.__password_hash == self.__hash_password(password):
            return True
        else:
            return False

    #Getter do cargo
    @property
    def role(self) -> str:
        return self.__role
    
    #Tratamento do cargo
    def __set_role(self, role):
        if role in ['admin', 'user', 'superadmin']:
            return role
        else:
            return None

    def __repr__(self):
        return f'{self.username}'
