
CS3090_Block2_Project
----------------------------------------
### Ted Staros
![Python](https://img.shields.io/badge/Python-3.12.3-blue)

---

CS3090_Block2_Project is a program that takes a user's password as a command argument in the terminal and returns a hexidecimal to show how the token would be stored in the database.

## Architecture
This program uses an API called Hashlib that receives a message from the user, encodes it and returns a hexidecimal


## Tech Stack:
- Python 3.12.3

##
Setup
* Clone or Fork this repository
* Follow these steps to install Python:
    * `Install Python, version 3.12.3`
    * `Follow instructions to download:` [Download Python](https://www.python.org/downloads/)
    * `Check python version: python --version or python3 --version`
    * `Make sure the version is 3.12.3`
##
Run The Program
* Enter the following in the command line once inside the project directory
    * `python (or python3) password_encryption "your password"`
    * `This will display a hexidecimal to the console that shows how the password would be securely saved in the database`
##
Warning
* This tool is for educational use only and should not be used for securing sensitive information
    * `sha256 not a good way to hash passwords, but susceptible to attackers because it computes hashes too quickly thus allowing attackers to use brute force to crack passwords. It also does not use salt so it is susceptible to attackers that use rainbow tables. For these reasons, it gives users a false sense of security`