#To print the factorial of any number'n' taken as input from the user
print("Enter number")
n=int(input())
def func(n):
   fac=1
   if n== 0:
      print(1)
   else:
      while n>=1:
        fac = fac*n
        n = n-1
      print(fac)

func(n)
