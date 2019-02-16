print("Enter a number")
n=int(input())
def func(n):
    if n==1:
        return 1
    return n*func(n-1)


def y(n):
    fact=0
    while(fact<1000):
         fact=func(n)
         if(fact<1000):
           print(fact,end=',')
           if(func(n+1)>1000):
             break
           n=n+1
         else:
           print("Sorry, the number entered has a factorial value>1000 please enter a smaller no.")
           break  

y(n)