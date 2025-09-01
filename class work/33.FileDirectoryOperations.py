# Read the files

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
    file.close()


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

#
try:
    with open('demo1.txt','r+') as file:
        print(f"Read entire content:\n{file.read()}\n")
    file.seek(0)
    print(f"Read only first line: {file.readline()}\n")
    file.seek(0)
    print(f"Return all the lines in a list:\n{file.readlines()}\n")
    file.write("\nSai Kumar\nAkash\nAdarsh")
    file.seek(0)
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File is not there")


# Append mode

try:
    with open('demo1.txt','a+') as file:
        file.write("End of the file")
        file.seek(0)
        print(file.read())
        file.close()
except FileNotFoundError:
    print("File is not there")

#
try:
    with open('demos.txt','w+') as file:
        file.write("End of the file")
        file.seek(0)
        print(file.read())
        file.close()
except Exception as e:
    print("Error Occured:,e")
