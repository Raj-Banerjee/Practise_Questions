def findfrequency(arr,n,x):
    count=int(0)
    for i in range(n):
        if arr[i]==x:
            count+=1
    return count
