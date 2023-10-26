import sys 
input = sys.stdin.readline

n = int(input());
arr = []

for i in range(n):
    arr.append((int(input()), i)) 

arr.sort();

top = 0;

for i in range(n):
    if  arr[i][1] - i > top :
        top =  arr[i][1] - i
    

print(top + 1)
