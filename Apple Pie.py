import time
from getpass import getpass
getpass ()

print ("Welcome to Mission Code Name Apple Pie")
print ("This is the login program.")
time.sleep (10)
mystring = "Opening Windows..."
print (mystring)
p1 = "Loading"
p2 = ".."
message = p1 + "." + p2
time.sleep (2)
print (message)

time.sleep (5)

correct = False
while correct == False:
    data = input ("\nPress any key to exit the Welcome Screen.")
    if data == "":
        correct = True
    else:
        pass

cnt = 0
correct = False
while correct == False:
    data = input ("\nPlease Enter Your Password: ")
    data = data.strip()
    if data == "isd273":
        time.sleep (1)
        print ("\nAccess Granted")
        correct = True
        time.sleep (1)
        print ("\nLoading Files...")
        time.sleep (5)
        print ("Preparing Desktop...")
    else:
        cnt += 1
        if cnt < 5:
            print ("\nAccess Denied. Please try again.")
        else:
            break

if cnt >= 5:
    print ("\n\tYou have maxed all attempts, please try again later.")

time.sleep (25)

cnt = 0
correct = False
while correct == False:
    data = input ("\nPlease Enter Your Password: ")
    data = data.strip()
    if data == "isd273":
        time.sleep (1)
        print ("\nAccess Granted")
        correct = True
        print ("\nLoading Files...")
        time.sleep (5)
        print ("Preparing Desktop...")
    else:
        cnt += 1
        if cnt < 2:
            print ("\nAccess Denied. Please try again.\n")
        else:
            break

if cnt >= 2:
    print ("\n\tYou have maxed all attempts, your account is now locked.")
    print ("\tPlease contact headquaters or reset your account to gain access.")
