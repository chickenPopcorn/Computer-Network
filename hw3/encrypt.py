# reading username and password from a local file
# encrypt username and password information
import hashlib

def read_user_info(filename):
    file = open('user_pass1.txt', 'w+')
    with open("user_pass.txt","r+") as f:
        for line in f:
            (uname, stored_pass) = line.split()
            print uname
            print stored_pass
            file.write(uname)
            file.write(" ")
            file.write(hashlib.sha1(stored_pass.encode()).hexdigest())
            file.write("\n")

read_user_info("user_pass.txt")
