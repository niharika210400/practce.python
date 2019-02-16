n=int(input())
def func(n):
    for i in range(n):
        for j in range(i):
           print('*',end=' ')
        print("\n")
func(n)        

#Method-2
m=int(input())
def func(m):
    print('pattern with',m,'lines')
    num=m
    while(num>0):
        print((m+1-num)*'*')
        num=num-1
func(m)
