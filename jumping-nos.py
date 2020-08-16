# Ques: https://practice.geeksforgeeks.org/problems/jumping-numbers/0
# Soln:
t=int(input(''))
while(t>0):
    t-=1
    n=int(input(''))
    print(0,end=' ')
    l=[str(i) for i in range(1,10)]
    while(len(l)>0):
        if(int(l[0])>n):
            break
        print(l[0],end=' ')
        if(ord(l[0][-1])==48):
            l+=[l[0]+chr(ord(l[0][-1])+1)]
        elif(ord(l[0][-1])<57):
            l+=[l[0]+chr(ord(l[0][-1])-1)]
            l+=[l[0]+chr(ord(l[0][-1])+1)]
        else:
            l+=[l[0]+chr(ord(l[0][-1])-1)]
        l=l[1:]
    print()
    
# Alt Approach
import threading, queue

def doThing():
    goal = int(input())
    li = queue.Queue()
    rtrn = []
    for i in range(10):
        li.put(i)
    
    rtrn.append(li.get())
    while ( not li.empty()):
        num = li.get()
        if(num <= goal):
            rtrn.append(num)
        rightmost = num%10
        
        if(not rightmost <= 0):
            temp = rightmost - 1
            if((num*10 + temp) <= goal):
                li.put(num * 10 + temp)
        if(not rightmost >= 9):
            temp = rightmost + 1
            if((num*10 + temp) <= goal):
                li.put(num * 10 + temp)

    for x in rtrn:
        print(x, end = " ")
    print()
