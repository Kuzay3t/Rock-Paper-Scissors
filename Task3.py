import random
# password generator

password_length = int(input("What is the lenght of the email adress you want? \n"))

uppercase_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
    "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", 
    ";", ":", "'", "\"", ",", ".", "/", "<", ">", "?", 
    "~", "`"]

 
def password_generator(password_length):
    pw = []
    while len(pw)<password_length:
        pw.append(random.choice(uppercase_letter))
        if len(pw) < password_length:
            pw.append(random.choice(lowercase_letter))
        if len(pw) < password_length:
            pw.append(random.choice(numbers))   
        if len(pw) < password_length:
            pw.append(random.choice(symbols))
    "________________________________________________________"

    random.shuffle(pw)
    return ''.join(map(str, pw[:password_length]))

print(f" The required password is '{password_generator(password_length)}'" )
    
#print(password_generator(password_length))