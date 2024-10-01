import string
import random
from tkinter import *


#initializing Tkinter

gui=Tk()                         # a basic application window is generated
gui.title("Password Generator")  #customizing application window
gui.geometry('400x350')          #sizing
gui.resizable(0,0)               #resizing of window by user is set to False

#adding Widgets to main window



#method for password generation
def Process():
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
    return All_pass


All_pass=Process()
print(All_pass)



