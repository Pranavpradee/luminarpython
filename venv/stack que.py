# que=[]
# size=int(input("enter the size :"))
# top=0
# n=0
# def enque():
#     global top,size
#     if (top>size):
#         print("que is full")
#     else:
#         eq=int(input("enter the element to enque"))
#         que.append(eq)
#         top+=1
# def deque():
#     global top,size
#     if(top<=0):
#         print("que is empty")
#     else:
#         que.deque()
#         top-=1
# def display():
#     print(que)
# while(n!=1):
#     print("enter the operation to perform :")
#     opt=int(input("press 1)enque 2)deque 3)display"))
#     if (opt==1):
#         enque()
#     elif (opt==2):
#         deque()
#     elif (opt==3):
#         display()
#     n=int(input("do you want to continue 0,press 1 to exit"))



#


que=[]
size=int(input("enter the size ::"))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print("que is full")
    else:
        p=int(input("enter the element to insert"))
        que.insert(rear,p)
        rear+=1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rare,size,que
    if rear==front:
        print("que is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print("enter the operation to perform")
    opt=int(input("press \n 1)enqueue \n 2) dequue \n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()


