# Ques: https://practice.geeksforgeeks.org/problems/finding-the-numbers/0
# Soln:
t = int(input())
for test in range(t):
    n = int(input())
    arr = [int(n) for n in input().split()]
    pairs = {}
    for i in arr:
        if i not in pairs:
            pairs[i] = 1
        else:
            del pairs[i]
    nums = [n for n in pairs.keys()]
    nums.sort()
    st = ""
    for sols in nums:
        st += str(sols) + " "
    print(st)
