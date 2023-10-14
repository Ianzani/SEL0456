"""
@author: Ian Zaniolo Sirbone
Title: Project 2
"""

from hashlib import sha256
from random import randint

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__role = self.set_role(role)
        self.__rand_number = randint(0,100)
        self.__password_hash = self.hash_password(password)
    #Getter do hash
    @property
    def password_hash(self):
        return self.__password_hash
    #Getter do cargo
    @property
    def role(self):
        return self.__role
    #Tratamento do cargo
    def set_role(self, role):
        if role in ['admin', 'user', 'superadmin']:
            return role
        else:
            return None
    #Função do hash com aleatoriedade
    def hash_password(self, password):
        password = str(self.__rand_number)+password
        return sha256(password.encode('utf-8')).hexdigest()
    #Função de verificação de senha
    def verify_password(self, password):
        if self.__password_hash == self.hash_password(password):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.username}'


def main():
    #Lista de usuarios
    users = list()

    #Criacao do primeiro usuario
    users.append(User('Ian', 'senha_forte', 'superadmin'))

    #Criacao do segundo usuario
    users.append(User('Teste', 'senha_fraca', 'user'))

    #Mostrando todos os usuarios
    for user in users:
        print(f'Nome de Usuário: {user}\nCargo: {user.role}\nHash da senha: {user.password_hash}\n')
    
    #Verificando senha dos usuarios
    for user in users:
        if user.verify_password('senha_forte'):
            print(f'Senha do {user} está correta')
        else:
            print(f'Senha do {user} está incorreta')

if __name__ == '__main__':
    main()
