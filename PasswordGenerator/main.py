import string
import random

if __name__== "__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    while True:
        try: #Expected input: Integer
            passlen=int(input("Enter password length\n"))
            break #breaks if user gives integer input
        except Exception as e: #while loop will keep running until valid input is given.
            print("Invalid Input! You need to type a number.")
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s) #shuffles characters of the list
    print("Your Password is: ")
    print("".join(s[0:passlen]))

    #Saving the passwords in a file 
    file=open("pass.txt","a")
    file.write("\n")
    file.write("".join(s[0:passlen]))
    file.close()

    print("Your password has been saved in a file")