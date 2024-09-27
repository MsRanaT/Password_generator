import string
import random


password=""
All_pass=[]
Pass_length=int(input("Enter length of password: "))

char_values=string.ascii_letters+string.digits+string.punctuation  #adding all alphabets,numbers and punc through this module string
x=0

while x<5:          #for generating 5 different passwords
    password=""
    for i in range(Pass_length):
        password+=(random.choice(char_values))
    print(password)

    All_pass.append(password)
    x+=1

print(All_pass)

