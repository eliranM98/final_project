import boto3
import os
def aws_read():
    f = open("C:/Users/gaga1/.aws/credentials", "r")
    print(f.read())
    c = open("C:/Users/gaga1/.aws/config", "r")
    print(c.read())

def aws_write():
    f = open("C:/Users/gaga1/.aws/credentials", "w")
    c = open("C:/Users/gaga1/.aws/config", "w")
    x = input("enter access key id: ")
    print(x)
    y = input("enter aws secret access key: ")
    print(y)
    z = input("enter a region: ")
    print(z)
    f.write("[default]\naws_access_key_id = " + x + "\naws_secret_access_key = " + y)
    c.write("[default]\nregion = " + z + "\noutput = json")
    f.close()
    c.close()
    aws_read()
aws_write()