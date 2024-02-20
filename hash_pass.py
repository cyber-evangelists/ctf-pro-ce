import hashlib

def hash_password(password):
   password_bytes = password.encode('utf-8')
   hash_object = hashlib.sha256(password_bytes)
   return hash_object.hexdigest()

if __name__ == "__main__":
    # Assumed password
    password = "#ExamplePassword"

    hashed_password = hash_password(password)
    print("Hashed password:", hashed_password)
