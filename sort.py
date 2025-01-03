def selection(list):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if(list[j]<list[min]):
                min=j
        temp=list[min]
        list[min]=list[i]
        list[i]=temp
n=int(input("how many elements"))
list=[]
for i in range(n):
    item=int(input())
    list.append(item)
print("unsorted list")
print(list)
selection(list)
print("sorted list")
print(list)
print("minimum element")
print([list[0]])
print("maximum element")
print(list[n-1])
