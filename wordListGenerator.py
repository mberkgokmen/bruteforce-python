import wordlist 

passwordInput = str(input("Letters, numbers, special characters to use : "))
firstInput = int(input("First : "))
lastInput = int(input("Last : "))

file = open("password.txt", "a")



def generatePassword(password, first, last):
    generator = wordlist.Generator(password)
    for passwords in generator.generate(first, last):
        print(passwords)
        file.write("\n")
        file.write(passwords)
        

generatePassword(passwordInput,firstInput,lastInput)

