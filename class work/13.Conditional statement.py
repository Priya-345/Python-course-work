#Conditional Statement
# Example 1 :
hr,mins = list(map(int,input("Enter the HH:MM  :").split(':')))
if hr>=0 and hr<=24 and mins>=0 and mins<=60:
    if hr>=0 and hr<4:
        print("Its a high time. Time to sleep")
    if hr>=4 and hr<12:
        print("Good Morning . Have a nice day")
    if hr>=12 and hr<16:
        print("Good Afternoon . Have a great Lunch")
    if hr>=16 and hr<20:
        print("Good evening . Have some snacks")
    if hr>=20 and hr<24:
        print("Good Night . Sweet dreams")
else:
    print("Enter the proper input,your input is invalid")

# Example 2:
data = {
    1:{'name':'Priyanka', 'exam_status':True , 'python':100 , 'sql':97 , 'html':95},
    2:{'name':'Revathi', 'exam_status':True , 'python':95 , 'sql':85 , 'html':65},
    3:{'name':'Nihitha', 'exam_status':True , 'python':98 , 'sql':87 , 'html':45},
    4:{'name':'sunitha', 'exam_status':None, 'python':None, 'sql':None , 'html':None},
    5:{'name':'Suma', 'exam_status':True , 'python':0 , 'sql':34 , 'html':50},
    }
stu_id=int(input("Enter the student id: "))
if stu_id in data:
    if data[stu_id]["exam_status"]:
        total=(data[stu_id]["python"]+data[stu_id]["sql"]+data[stu_id]["html"])/3
        if total>90:
            print(f"Congrats!!!!{data[stu_id]['name']}\nYou got 'A' grade")
        elif total>75:
             print(f"Good JOb!!!!{data[stu_id]['name']}\nYou got 'B' grade")
        elif total>45:
             print(f"Need Imporvement!!!!{data[stu_id]['name']}\nYou got 'C' grade")
        elif total>35:
             print(f"{data[stu_id]['name']}Just Passed\nYou got 'D' grade")
        elif total<35:
             print(f" Better luck next time {data[stu_id]['name']}\n You have failed the exam")
    else:
        print(f"{data[stu_id]['name']} is not attempted the exams")
else:
    print("Invalid Student id")
            


# Example 3:
Seats = {
    'L1':True,
    'l2':False,
    'l3':False,
    'l4':True,
    'U1':True,
    'u2':False,
}
seatno = input("Enter the seat no to check its availability:").upper()
if seatno in Seats:
    if Seats[seatno]:
        print("Already Booked.Try with other number")
    else:
        print("Seat is available.Hurry Up")
else:
    print("Enter the correct seat number")



# Example 4:
data={
    'watch':{'discount':10,'brands':['titan','fastrack']},
    'facewash':{'discount':24,'brands':['garnier','mamaearth','cleanandclear']},
    'tops':{'discount':15,'brands':['max','h&m','Zara']},
    'shrits':{'discount':44,'brands':['polo','panamerican','peterinland']},
    'jeans':{'discount':54,'brands':['demin','roadsiter']},
}
print(data.keys())
pro=input("Enter the cat : ")
if pro in data:
    print(f'{data[pro] ["discount"]}% discount is going on for this brands: {data[pro]["brands"]}')
else:
    print(f"Product is out of stock. Please check with other products: {data}")


# Example 5:
movies={
    'salar':{'kids':True},
    'Rajarani':{'kids':True},
    'Kannapa':{'kids':False},
    'Masudha':{'kids':False},
    'Arjunreddy':{'kids':False},
    'Littlestarts':{'kids':True},
}
print('Welcome to hotstar'.center(30,'='))
movie=input("Enter the movie: ").title()
if movie in movies:
    if movies[movie]['kids']:
        print(f"Good selection.You can watch with your family\n{movie}.......")
    else:
        print(f"Adult Movie.Kids are not allowed.\n{movie}..............")
else:
    print(f"{movie} is not available")


# Example 6:
data={
    'INDIA':('passport',),
    'NEPAL':('passport',),
    'USA':('passport','visa'),
    'CANADA':('passport','visa'),
    'ENGLAND':('passport','visa'),
}
from_place=input("Enter the place from where you want to go: ")
to_place=input("Enter the place you want to go: ").upper()
if to_place in data:
    if len(data[to_place])==1:
       print(f"Great .You only need a passport to viosit {to_place}")
    else:
        print(f" Great.You need  passport and visa to vist {to_place}")
else:
    print(" No data available")





