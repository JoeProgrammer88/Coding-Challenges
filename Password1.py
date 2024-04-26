import hashlib
import itertools
from multiprocessing import Pool

# Create a list of ASCII characters for digits 0-9
digits = [chr(i) for i in range(48, 58)]  # 0-9

def check_password(password_tuple):
    # Join the tuple elements to form the password string
    password = ''.join(password_tuple)

    # if password is divisible by 1 million print it
    if int(password) % 1000000 == 0:
        print(f"Checking password: {password}")

    # Create a new md5 hash object
    hash_object = hashlib.md5()

    # Hash the generated password
    hash_object.update(password.encode())

    # Convert the hash object into a hexadecimal string
    hash_hex = hash_object.hexdigest()

    # Check if the hashed password starts with "351635d71448baca"
    if hash_hex.startswith("351635d71448baca"):
        # If it does, return the password
        return password

def find_password():
    # itertools.product generates Cartesian product from the digits list, repeated 12 times (for 12-digit password)
    passwords = itertools.product(digits, repeat=12)

    # Create a pool of 12 worker processes
    with Pool(24) as p:
        # Map the check_password function to the passwords iterable
        for result in p.imap(check_password, passwords):
            if result is not None:
                print(f"Password found: {result}")
                break
        else:
            print("Password not found!")

if __name__ == '__main__':
    # Call the function to find the password
    find_password()
