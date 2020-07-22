#Prompt 1 (Stone's Love)
first = input()
N = input()
Q = input()
N = N.split()
Q = Q.split()


for i in range(len(Q)):
    total = 0
    for j in range(len(N)):
        total += int(N[j])
        if total >= int(Q[i]):
            print(j+1)
            break
            
            
# Prompt 2 (Repeated K times)
N = int(input())
arr = input()
arr = arr.split()
b = sorted(set(arr))
k = int(input())

for i in b:
    if arr.count(i) == k:
        print(i)
        break
