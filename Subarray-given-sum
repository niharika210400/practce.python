#code
t = int(input())
def subArraySum(arr, n, sum): 
    curr_sum = arr[0] 
    start = 0
  
    i = 1
    while i <= n: 
        while curr_sum > sum and start < i-1: 
          
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == sum: 
            print (start+1, i) 
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
  
    # If we reach here,  
    # then no subarray 
    print (-1) 
    return 0
    
for j in range(t):
    n,sum = map(int,input().split())
    arr = list(map(int,input().split()))
    subArraySum(arr, n, sum)
