from functions import *

def main():
    correct_password = 'teste'

    with open('password_hash.txt', 'w') as file:
        file.write(hash_password(correct_password))

    with open('password_entry.txt', 'r') as file:
        for line in file:
            print(f'A senha presente no arquivo de texto é: {line}')

    if verify_password():
        print('Senha correta!')
    else:
        print('Senha incorreta!')

if __name__ == '__main__':
    main()