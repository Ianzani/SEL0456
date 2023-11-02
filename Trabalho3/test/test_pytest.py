from main import password_entry_dir, password_hash_dir
from functions import verify_password

def test_password():
    assert verify_password(password_hash_dir, password_entry_dir)
