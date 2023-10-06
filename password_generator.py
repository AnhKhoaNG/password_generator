import secrets
import string 

def password_generator(length,contain_num=True,contain_special_char=True):
    letters = string.ascii_letters
    numbers = string.digits
    special_char = string.punctuation
    
    avai_char = letters # Available characters
    if contain_num == True: #Adding digits if the users want
        avai_char+=numbers
    if contain_special_char == True: #Adding special characters if the users want
        avai_char+= special_char
    while True:  #Generating Password based on constraints of the users
        password = ""
        for i in range(length):
            password += ''.join(secrets.choice(avai_char))
        if contain_special_char and not contain_num:
            if any(char in special_char for char in password):
                break
        elif contain_num and not contain_special_char:
            if sum(char in numbers for char in password)>=1:
                break
        elif contain_special_char and contain_num:
            if (any(char in special_char for char in password) and sum(char in numbers for char in password)>=1):
                break
        else:
            break
    return password
    
def main():
    length = int(input("Enter length of your password: "))
    while length <8:
        length = int(input("Your password must be at least 8 characters long. Please enter again: "))
    contain_num = input("Do you want it to contain num? Answer with y/n: ").lower() == "y" 
    contain_special = input("Do you want it to contain special char? Answer with y/n: ").lower() == "y" 
    password= password_generator(length,contain_num,contain_special)
    print("This is your generated password:",password)
    
main()