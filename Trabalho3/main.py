from functions import hash_password
import os

correct_password = 'teste'

current_dir = os.path.dirname(os.path.abspath(__file__))
password_hash_dir = os.path.join(current_dir, 'password_hash.txt')
password_entry_dir = os.path.join(current_dir, 'password_entry.txt')

def main():

    with open(password_hash_dir, 'w') as file:
        file.write(hash_password(correct_password))

if __name__ == '__main__':
    main()