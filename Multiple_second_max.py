
Marksheet = [[ input(), float(input())] for i in range(int(input()))]
Report = sorted(set([x[1] for x in Marksheet]))
for name in sorted(x[0] for x in Marksheet if x[1] == Report[1]):
    print(name)
