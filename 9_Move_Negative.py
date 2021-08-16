'''
{
    Given an unsorted array arr[] of size N having both negative and positive integers. 
    The task is place all negative element at the end of array 
    without changing the order of positive element and negative element.

    Input : 
    N = 8
    arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
    Output : 
    1  3  2  11  6  -1  -7  -5

    link: https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1
}
'''

arr = [1, -1, 3, 2, -7, -5, 11, 6 , 6]
size=len(arr)
arr2=[]
for i in range(size):
    #print(arr[i])
    if(arr[i]<0):
        #print("Y")
        arr2.append(arr[i])
        #print("Y")
arr = [item for item in arr if item >= 0]
arr=arr+arr2



print(arr)
#print(arr2)
#print(arr1)
