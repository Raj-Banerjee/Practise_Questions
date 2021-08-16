'''
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.
Example

Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max =  10000
link: https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
'''

size=int(input())
while(size>0):
    
    arr=list(map(int,input().split(" ")))
    arr.sort()
    print("min= ",arr[0],end=" ")
    print("max= ",arr[size-1])
    
    break