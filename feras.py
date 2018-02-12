print("if you want to start the game enter 1")
print("if you want to closse the game enter 2")
w=int(input())
while w==1:
    from math import *
    from random import *
    L1=[]
    L2=[]
    p1=[]
    p2=[]
    z='_'
    size=randint(10 , 20)
    for s in range(size):
        L1.append(s)
        L2.append(z)
    print(L1)
    for i in  L1:
        print("p1:are you want enter one number or two")
        a=int(input())
        while True:
            if a!=1 and a!=2:
                print('you should enter 1 or 2')
                a=int(input('enter 1 or2\n'))
            if a==1:
                print("enter the number")
                x1=int(input())
                while True :
                    if x1 in p1:
                        print("you are entered this number before")
                        print("enter a new number")
                        x1=int(input())
                        del L1[x1]
                        L1.insert(x1,z)
                    if x1 in p2:
                        print("erorr you enter number it was entered")
                        print("enter a new number ")
                        x1=int(input())
                        del L1[x1]
                        L1.insert(x1,z)
                    elif x1 not in p1 or p2 :
                        del L1[x1]
                        L1.insert(x1,z)
                    if x1 in p2:
                        continue
                    if x1 in p1:
                        continue
                    else:
                        break
                p1.append(x1)    
                print(L1)
                break
            elif a==2:
                print("enter the first number and the second will be 'first+1'")
                x1=int(input())
                x2=x1+1
                while True:
                    if x1 in p1:
                        print("this number entered before")
                        print("enter a new number")
                        x1=int(input())
                        x2=x1+1
                    if x1 in p2:
                        print("this number entered before")
                        print("enter a new number")
                        x1=int(input())
                        x2=x1+1
                    if x2 in p2:
                        print("erorr the second number entered before")
                        print("enter the first number agien and the second will be 'first+1'")
                        x1=int(input())
                        x2=x1+1
                    if x2 in p2:
                        print("erorr the second number entered before")
                        print("enter the first number agien and the second will be 'first+1'")
                        x1=int(input())
                        x2=x1+1
                    if x2 and x1 not in p1 and p2:
                        break
                    if x2  in p2:
                        continue
                    if x1 in p2:
                        continue
                    if  x1 in p1:
                        continue
                    if x2 in p1:
                        continue
                    else:
                        break
                p1.append(x2)
                del L1[x1]
                L1.insert(x1,z)
                del L1[x2]
                L1.insert(x2,z)
                p1.append(x1)
                print(L1)
                break
        if L1==L2:
            print("p1:you are won")
            print(L2)
            break
        print("p2:are you want enter one number or two")
        a=int(input())
        while True:
            if a!=1 and a!=2:
                print('you should enter 1 or 2')
                a=int(input('enter 1 or 2\n'))
            if a==1:      
                print("enter the first number")
                y1=int(input())
                while True:
                    if y1 in p2:
                        print("you are entered this number before")
                        print("enter a new number")
                        y1=int(input())
                        del L1[y1]
                        L1.insert(y1,z)
                    if y1 in p1:
                        print("erorr you enter number it was entered")
                        print(" enter a new number ")
                        y1=int(input())
                        del L1[y1]
                        L1.insert(y1,z)
                    elif y1 not in p1 or p2 :
                        del L1[y1]
                        L1.insert(y1,z)
                    if y1 in p2:
                        continue
                    if y1 in p1:
                        continue
                    else:
                        break
                p2.append(y1)
                print(L1)
                break
            elif a==2:
                print("enter the first number and the second will be 'first+1'")          
                y1=int(input())
                y2=y1+1
                while True:
                    if y1 in p2:
                        print("this number entered before")
                        print("enter a new number")
                        y1=int(input())
                        y2=y1+1
                    if y1 in p1 :
                        print("this number entered before")
                        print("enter a new number")
                        y1=int(input())
                        y2=y1+1
                    if y2 in p2:
                        print("erorr the second number entered before")
                        print("enter the first number agien and the second will be 'first+1'")
                        y1=int(input())
                        y2=y1+1
                    if y2 in p1:
                        print("erorr the second number entered before")
                        print("enter the first number agien and the second will be 'first+1'")
                        y1=int(input())
                        y2=y1+1
                    if y2 and y1 not in p1 and p2:
                        break
                    if y1 in p2:
                        continue
                    if y2 in p2:
                        continue
                    if  y1 in p1:
                        continue
                    if y2 in p1:
                        continue
                    else:
                        break
                p2.append(y2)
                del L1[y1]
                L1.insert(y1,z)
                del L1[y2]
                L1.insert(y2,z)
                p2.append(y1)
                print(L1)
                break    
        if L1==L2:
            print("p2:you are won")
            print(L2)
            break
    print("if you want to try agian enter 1")
    print("if you want to closse the game enter 2")
    w=int(input())
