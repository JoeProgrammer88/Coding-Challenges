import hashlib

hash_object = hashlib.md5()

hash_object.update(b"Ok, got it. Easy!")

hash_hex = hash_object.hexdigest()

# Print the first 5 characters of the hexadecimal hash
print(hash_hex[:5])