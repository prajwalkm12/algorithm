import random
import time
import sys
def partition(a,low,high):
    pe=a[high]
    i=low
    j=high
    while true:
        while i<j and a[i]<=pe:
            i=i+1
        while i<j and a[j]>=pe:
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[i]
        else:
            break
    a[i],a[high]=a[high],a[i]
    return i
def quicksort(a,low,high):
    if low<high:
        pq=partition(a,low,high)
        quicksort(a,low,high)
        quicksort(a,pq+1,high)
n=500
list=[random.randint(1,1000) for in range(n)]
with open("outputquick.txt","w")as file:
    sys.stdout=file
    print("unsorted elements of the list")
    print(list)
    start_time=time.time()
    quicksort(list,0,n-1)
    end_time=time.time()
    print("sorted elements of the list")
    print(list)
    execution_time=end_time-start_time
    print(f"execution time:{execution_time} seconds")
    sys.stdout=sys__stdout__