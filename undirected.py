#indegree and outdegree undirected graph
def graphdeg(arr,n,v):
	print("adjacency matrix")
for i in range(n):
    print(arr[i])
for i in range(n):
    ccnt=0
    rcnt=0
    for j in range(n):
        if(arr[i][j]!=0):
            rcnt+=1
        if(arr[j][i]!=0):
            ccnt+=1
        print("indegree of",v[i],"is",ccnt)
        print("outdegree of",v[i],"is",rcnt)
n=int(input("how many vertices?"))
print("enter the vertices")
v=[]
for i in range(n):
    v.append(input())
arr=[]
for i in range(n):
    arr2=[]
    arr1.append(arr2)
print("is there any incidence from")
for i in range(n):
    if(i==j):
        arr1[i].insert(j,0)
        continue
    if(i<j):
        print(v[i],"is",v[j])
        num=int(input())
        arr1[i].insert(j,num)
        arr1[j].insert(i,num)
graphdeg(arr1,n,v)