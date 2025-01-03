def find_min_max(arr,low,high):
    if low==high:
        return arr[low],arr[low]
    if high-low==1:
        return(arr[low],arr[high] if arr[low]<arr[high] else arr[high],arr[low])
    mid=(low+high)//2
    min1,max1=find_min_max(arr,low,mid)
    min2,max2=find_min_max(arr,mid+1,high)
    return min(min1,min2),max(max1,max2)
my_list=[]
n=int(input("enter the size of list"))
for i in range(n):
        my_list.append(int(input()))
min_value,max_value=find_min_max(my_list,0,len(my_list)-1)
print("minimum element",min_value)
print("maximum element",max_value)
