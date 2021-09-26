#Created and code by Shiv

import  random as rm
import string


def output(length):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    rm.shuffle(characters)
    password = []
    for i in range(length):
        password.append(rm.choice(characters))
    print("".join(password))


def passwd_generate():
      try:
          length = int(input("Enter the length of password : "))
          output(length)
      except:
          print("Enter valid number and try again")
          passwd_generate()

print("******** Welcome to password Generator ****** \n")

passwd_generate()

input(" \n Please press Enter to exit the code :) \n ")