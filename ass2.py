password=input("Enter your Password:")

def check(password):
    if len(password)>=8:
        uppercase=False
        lowercase=False
        has_digit= False
        has_special= False
        special_char= "@#$%&"

        for ch in password:
            if ch.isupper():
                uppercase=True
            elif ch.islower():
                lowercase=True
            elif ch.isdigit():
                has_digit=True
            elif ch in special_char:
                has_special = True
        
        if uppercase and lowercase and has_digit and has_special:
            return "Valid Password"
        else:
            return "Invalid Password"

result=check(password)
print(result)