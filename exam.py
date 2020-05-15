import random

#=====Davaleba 1 =====#
nums=[]
for i in range(10,3000):
    if i%2==1 and (i/7).is_integer():
        nums.append(i)
print(nums)

#=====Davaleba 2 =====#
str="4,5,6,13"
arr=[int(n) for n in str.split(",")]
print(arr)

#=====Davaleba 3 =====#
print("Enter Value for M:")
M=int(input())
print("Enter Value for N:")
N=int(input())
MatX=[[0 for x in range(M)] for y in range(N)];
for x in range(M):
    MatX[0][x]=random.randrange(0,10)

for x in range(1,M):
    for y in range(N):
        MatX[x][y]=MatX[x-1][y]*2
for row in range(M):
    print(MatX[row])
    
#=====Davaleba 4 =====#
words=input().split(";")
for x in range(0,len(words)):
    print(sorted(words[x]))