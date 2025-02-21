import hashlib
import sys

password = sys.argv[1]

secure_token = hashlib.sha256(password.encode()).hexdigest()

print(secure_token)