'''
Check if a key is present in every segment of size k in an array.
Given an array arr[] and size of array is n and one another key x, and give you a segment size k. 
The task is to find that the key x present in every segment of size k in arr[].
Link: https://www.geeksforgeeks.org/check-if-a-key-is-present-in-every-segment-of-size-k-in-an-array/
'''

def findkey(arr,size,key):
    length=int(len(arr))
    section=length//size

    # Check for no of times the file needs to be rotated
    if((section)!=(length/size)):
        section+=1

    counter=int(0)
    term=int(0)    

    for i in range(0,section):
        a=arr[term:term+size]
        if(key in a):
            counter+=1
        
        term=term+size

    if(counter==section):
        print("Yes")

    else:
        print("No")


arr=[3,4,5,3,9,1,1,3,2,3,3,6,8,7,3,3]
size=int(3)
key=int(3)
findkey(arr,size,key)
