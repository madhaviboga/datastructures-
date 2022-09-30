def Insertionsort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while a[j]>key and j>=0:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=key
a=[5,9,3,1,7]
Insertionsort(a)
l=[]
print("sorted array is:")
for i in range(len(a)):
    l.append(a[i])
print(l)
            