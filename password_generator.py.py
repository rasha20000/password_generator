import random
import string
def generate_password (lengyh=12) :
    #all possible letters , symbols and numbers
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    #random letters
    password = ''.join(random.choice(characters) for i in range(length))
    return  password 

if __name__ == "__main__":
    l = input("How long a password do you want?")
    try :
        length = int(l)
        new_password = generate_password(length)
        print ('Your new password is :',new_password )
    except :
        print ("please inter a number")
    