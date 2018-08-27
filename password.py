
#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
birthday = input("What year were you born in?")
test_password = input("Type in a trial password: ")


for line in f:
    if test_password.strip() == line.strip():
        print("This is a weak password")
    elif test_password.lower() == line.strip():
        print("This is a weak password")
    elif test_password.lower() == line.strip()+"2018":
        print("This is a weak password")
    elif test_password.lower() == line.strip()+birthday:
        print("This is a weak password")
    elif test_password.datetime() == line.strip():
        print("This is a weak password")


#Write logic to see if the password is in the dictionary file below here:
