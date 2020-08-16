# Ques: https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1
# Soln:
''' Your task is to returns 1 if there is triplet with sum equal
    to 0 present in arr[], else return 0'''

def findTriplets(arr, n): 
    sum = 0
    for i in range(0, n-1): 
        # Find pair in subarray A[i + 1..n-1]  
        # with sum equal to sum - A[i] 
        s = set() 
        curr_sum = sum - arr[i] 
        for j in range(i + 1, n): 
            if (curr_sum - arr[j]) in s: 
                return 1
            s.add(arr[j]) 
      
    return 0


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        print(findTriplets(a,n))
# } Driver Code Ends




# Alt Soln:
''' Your task is to returns 1 if there is triplet with sum equal
    to 0 present in arr[], else return 0'''
    
def findTriplets(arr,n):
    found = 0
    for i in range(n - 1): 
  
        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                found = 1
            else: 
                s.add(arr[j]) 
    return found



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        print(findTriplets(a,n))
# } Driver Code Ends

