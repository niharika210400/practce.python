# Ques: https://practice.geeksforgeeks.org/problems/longest-valid-parentheses/0
# Soln:
t = int(input())

def findMaxLen(s): 
    if (len(s) <= 1): 
        return 0
      
    # Initialize curMax to zero  
    curMax = 0
  
    longest = [0] * (len(s)) 
  
    # Iterate over the string starting  
    # from second index 
    for i in range(1, len(s)): 
        if ((s[i] == ')' and 
             i - longest[i - 1] - 1 >= 0 and 
             s[i - longest[i - 1] - 1] == '(')):  
                longest[i] = longest[i - 1] + 2
                if (i - longest[i - 1] - 2 >= 0): 
                    longest[i] += (longest[i - 
                                   longest[i - 1] - 2]) 
                else: 
                    longest[i] += 0
                curMax = max(longest[i], curMax) 
    return curMax 

for _ in range(t):
    s = input()
    print(findMaxLen(s))
