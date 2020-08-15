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

# Alternate Approach

# Function to return the length of 
# the longest valid substring 
def solve(s, n): 
	
	# Variables for left and right counter. 
	# maxlength to store the maximum length found so far 
	left = 0
	right = 0
	maxlength = 0
	
	# Iterating the string from left to right 
	for i in range(n): 
		
		# If "(" is encountered, 
		# then left counter is incremented 
		# else right counter is incremented 
		if (s[i] == '('): 
			left += 1
		else: 
			right += 1
			
		# Whenever left is equal to right, it signifies 
		# that the subsequence is valid and 
		if (left == right): 
			maxlength = max(maxlength, 2 * right) 
			
		# Reseting the counters when the subsequence 
		# becomes invalid 
		elif (right > left): 
			left = right = 0
			
	left = right = 0
	
	# Iterating the string from right to left 
	for i in range(n - 1, -1, -1): 
		
		# If "(" is encountered, 
		# then left counter is incremented 
		# else right counter is incremented 
		if (s[i] == '('): 
			left += 1
		else: 
			right += 1
			
		# Whenever left is equal to right, it signifies 
		# that the subsequence is valid and 
		if (left == right): 
			maxlength = max(maxlength, 2 * left) 
			
		# Reseting the counters when the subsequence 
		# becomes invalid 
		elif (left > right): 
			left = right = 0
	return maxlength 


# Driver code 

print(solve("((()()()()(((())", 16))
