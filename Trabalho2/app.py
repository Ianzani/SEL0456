"""
@author: Ian Zaniolo Sirbone
Title: Project 2
"""

from users import User

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
    print('Verificação antes da alteração da senha:')
    for user in users:
        if user.verify_password('senha_forte'):
            print(f'Senha do {user} está correta')
        else:
            print(f'Senha do {user} está incorreta')

    #Alterando senha do usuário teste
    users[1].change_password('senha_fraca', 'senha_forte')
    print('\nVerificação após a alteração da senha:')

    #Verificando novamente a senha dos usuários
    for user in users:
        if user.verify_password('senha_forte'):
            print(f'Senha do {user} está correta')
        else:
            print(f'Senha do {user} está incorreta')

if __name__ == '__main__':
    main()