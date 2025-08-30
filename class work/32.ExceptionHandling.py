#
'''
try:
    a=12/6
    b=int(input("Enter the int: "))
    c=3+6
    d={1:2 ,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    c=a+e
except ZeroDivisionError:
    print("Can't divide with zero")
except ValueError:
    print("Please enter the properly datatype")
except TypeError:
    print("We can't add 2 diff types")
except KeyError:
    print("We don't have that key")
except IndexError:
    print("We don't have that key")
except NameError:
    print("Please define the var")'''



##
'''
try:
    a=12/6
    b=int(input("Enter the int: "))
    c=3+6
    d={1:2 ,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    c=a+e
except (ZeroDivisionError,ValueError,TypeError,KeyError,IndexError,NameError):
    print("Error Occured")'''

##
'''
try:
    a=12/6
    b=int(input("Enter the int: "))
    c=3+6
    d={1:2 ,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    c=a+e
except (ZeroDivisionError,ValueError,TypeError,KeyError,IndexError,NameError) as e:
    print("Error Occured:  {e}")'''

##
'''
try:
    a=12/6
    b=int(input("Enter the int: "))
    c=3+6
    d={1:2 ,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    c=a+e
except Exception as e:
    print(f"Error Occured: {e}")'''

##
try:
    a=12/6
    b=int(input("Enter the int: "))
    c=3+6
    d={1:2 ,2:4,3:6,4:8}
    i=d[2]
    l=[0,1,2,3]
    m=l[1]
    e=2
    c=a+e
except Exception as e:
    print(f"Error Occured: {e}")
else:
    print("Error frees")
finally:
    print("End of the program")