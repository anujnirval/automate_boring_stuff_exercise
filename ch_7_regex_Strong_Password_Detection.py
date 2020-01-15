import re

password = input("Enter a strong password:\n")
print("Validating the password agains password policy")

pwdRegex1 = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')

def checkPassword(text):
    if pwdRegex1.search(text):
        return True
    else:
        return False

print("Password match result is:\n"+str(checkPassword(str(password))))
