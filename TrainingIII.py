'''
Ok, pushing a string through a hash function is easy. If you go forwards. How about backwards? This might require a bit more force. Maybe even brute force?

The next password consists of three characters [a-z,A-Z,0-9].
Not order specific!
The md5-hash of the password begins with 19acf8371f
'''
import hashlib

# Loop through all possible 3 characters strings that can only contain
# [a-z,A-Z,0-9] and hash them until we find the one that starts with
# 19acf8371f
def find_password():
    # Create a while loop that will run until the password is found
    # The loop will iterate through all possible 3 character strings
    # that can only contain lowercase or uppercase a - z and 0 - 9
    # characters
    password = ""
    while True:
        for digitChar in range(48, 58): # 0-9
            for uppercaseChar in range(65, 91): # A-Z
                for lowercaseChar in range(97, 123): # a-z
                    password =  chr(digitChar) + chr(uppercaseChar) + chr(lowercaseChar)
                    hash_object = hashlib.md5()
                    hash_object.update(password.encode())
                    hash_hex = hash_object.hexdigest()
                    if hash_hex.startswith("19acf8371f"):
                        return password
                
print(find_password())