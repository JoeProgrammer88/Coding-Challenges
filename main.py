import hashlib

hash_object = hashlib.md5()

hash_object.update(b"Ok, got it. Easy!")

hash_hex = hash_object.hexdigest()

print(hash_hex)
