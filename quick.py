from array import*
def partition(ar,low,high):
    pivot=ar[low]
    i=low+1
    j=high
    while(true):
        while((i<=j) and (ar[i]<=pivotE)):
            i=i+1
        while((i<=j) and (ar[j]>=pivotE)):
            j=j-1
        if(i<=j):
            ar[i],ar[j]=ar[j],ar[i]
        else:
            break
    ar[low],ar[j]=ar[j],ar[low]
    return j
def quicksort(ar,firstEI,lastEI):
    if(firstEI<lastEI):
        pivotEI=partition(ar,firstEI,lastEI)
        quicksort(ar,firstEI,pivotEI-1)
        quicksort(ar,pivotEI+1,lastEI)
intArr=array('i',[])
n=int(input("how many elements?"))
print("enter the list of {} elements".format(n))
for i in range(n):
    intArr.append(int(input()))
print("list of elements before sorting them")
print(intArr)
quicksort(intArr,0,len(intArr)-1)
print("list of elements after sorting them")
print(intArr)