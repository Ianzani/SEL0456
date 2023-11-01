from functions import *
import os

def main():
    correct_password = 'teste'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    password_hash_dir = os.path.join(current_dir, 'password_hash.txt')
    password_entry_dir = os.path.join(current_dir, 'password_entry.txt')

    with open(password_hash_dir, 'w') as file:
        file.write(hash_password(correct_password))

    with open(password_entry_dir, 'r') as file:
        for line in file:
            print(f'A senha presente no arquivo de texto é: {line}')

    if verify_password(password_hash_dir, password_entry_dir):
        print('Senha correta!')
    else:
        print('Senha incorreta!')

if __name__ == '__main__':
    main()