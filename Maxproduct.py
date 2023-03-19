class Solution:
    def maxTripletProduct (self, arr): 
            #Complete the function
            arr.sort()
            return max(arr[0] * arr[1] * arr[-1], arr[-3] * arr[-2] * arr[-1])
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

for _ in range(0,int(input())):
    n=int(input())
    arr=[]
    for i in range (n):
         arr.append(int(input()))
    
    ob=Solution()
    res = ob.maxTripletProduct(arr)
    print(res)
# } Driver Code Ends