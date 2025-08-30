# Nested exception

try:
   a=int(input())
   b=int(input())
   try:
       c=a/b
   except Exception as e:
    print(f"Error Occured: {e}")
except Exception as e:
    print(f"Error Occured: {e}")
else:
    print("Error frees")
finally:
    print("End of the program")


