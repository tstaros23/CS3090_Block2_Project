import hashlib
import sys
'''
Author Ted Staros
This tool is for educational use only and should not be used for securing sensitive information
'''
password = sys.argv[1]

secure_token = hashlib.sha256(password.encode()).hexdigest()

print(secure_token)