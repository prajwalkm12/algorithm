from array import*
def mergesort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        leftSA=arr[:mid]
        rightSA=arr[mid:]
        mergesort(leftSA)
        mergesort(rightSA)
        i=0
        j=0
        k=0
        while(i<=len(leftSA) and j<len(rightSA)):
            if(leftSA[i]<=rightSA[j]):
                arr[k]=leftSA[i]
                i=i+1
            else:
                arr[k]=rightSA[j]
                j=j+1
            k=k+1
        while(i<len(leftSA)):
            arr[k]=leftSA[i]
            i=i+1
        while(j<len(rightSA)):
            arr[k]=rightSA[j]
            j=j+1
            k=k+1
arr=array('i',[])
num=int(input("how many elements you want to sort"))
print("enter {} element".format(num))
i=0
while(i<num):
    arr.append(int(input()))
    i=i+1
print("unsorted elements")
print(arr)
mergesort(arr)
print("sorted elements")
pri(arr)