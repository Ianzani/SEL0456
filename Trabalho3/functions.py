from hashlib import sha256


def hash_password(password) -> str:
    return sha256(password.encode('utf-8')).hexdigest()

def verify_password() -> bool:

    with open('password_entry.txt', 'r') as file:
        for line in file:
            password = line

    with open('password_hash.txt', 'r') as file:
        for line in file:
            password_hash = line

    if password_hash == hash_password(password):
        return True
    else:
        return False