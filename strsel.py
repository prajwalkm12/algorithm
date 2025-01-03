from array import *
arr=[]
n=int(input("how many elements"))
print('enter {} elements'.format(n))
for i in range(n):
    arr.append(input())
for i in range(n):
    min=i
    for j in range(i+1,n):
        if(arr[j]<arr[min]):
            min=j
    temp=arr[min]
    arr[min]=arr[i]
    arr[i]=temp
print("after sorting")
for i in range(n):
    print(arr[i])