#ASSignment
n = int(input("Enter the no of messages: "))
chat={}
for i in range(n):
    name,msg=input().split(':')
    if name in chat:
        chat[name].append(msg.strip())
    else:
        chat[name]=[(i,msg.strip())]
while True:
    print("count the no of messages")
    print("2.Identify unique users in the chat")
    print("0.Exit\n")
    ch=int(input("Enter your choice: "))
    if ch==0:
        break
    elif 1<=ch<=18:
        if ch==1:
            total_msg=0
            for i in chat:
                total_msg+=len(chat[i])
                print(f"Total number of messages: {total_msg}")
        elif ch==2:
            print("unique users in chat")
            for i,key in enumerate(chat):
                print(f'{i+1}.{key}')
    else:
        print("Invalid choice")