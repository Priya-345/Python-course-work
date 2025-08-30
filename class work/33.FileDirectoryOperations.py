# Read the files
'''
try:
    file = open('demo1.txt','r')
except FileNotFoundError:
    print("File is not there")
else:
    print(f"Read entire content:\n{file.read()}\n")
    file.seek(0)
    print(f"Read only first line: {file.readline()}\n")
    file.seek(0)
    print(f"Return all the lines in a list:\n{file.readlines()}\n")
    file.close()'''


#
try:
    file = open('demo1.txt','r+')
except FileNotFoundError:
    print("File is not there")
else:
    print(f"Read entire content:\n{file.read()}\n")
    file.seek(0)
    print(f"Read only first line: {file.readline()}\n")
    file.seek(0)
    print(f"Return all the lines in a list:\n{file.readlines()}\n")
    file.write("\nSai Kumar\nAkash\nAdarsh")
    file.seek(0)
    print(file.read())
    file.close()
