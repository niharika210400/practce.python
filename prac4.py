N=int(input())
if((N>=1)and(N<=100)):
 if((N%2)==1):
  print("Weird")
 elif(((N>=2)and(N<=5))or(N>20)):
  print("Not Weird")
 elif((N>=6)and(N<=20)):
  print("Weird")
 else:
  pass
else:
 print("Invalid input")
