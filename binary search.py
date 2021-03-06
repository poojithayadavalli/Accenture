"""
Given a sorted array of integers and a key to be searched in the array. Print the position of the key in the array, if present.

If it's not present in the array, print -1. 

Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise.

Constraints:
1 <= T <= 100
1 <= N <= 104

Input:
The first line contains an integer 'T' denoting the number of test cases. 
Then 'T' test cases follow. Each test case consists of 3 lines. 
First line of each test case contains an integer N denoting the size of the array.
Second line of each test case consists of 'N' space separated integers denoting the elements of the array A[]. 
The third line contains a key 'k' .

Output:
Prints the position of the key if its present in the array else print -1 if the key is not present in the array.


1 <= arr[i] <= 104

Example:
Input:
2
5
1 2 3 4 5 
4
5
11 22 33 44 55
445

Output:
3
-1

Explanation:
Test Case 1:
4 is present at the index 3 (0-based) in the array.

Test Case 2:
Since 445 is not present in the given array, we return -1.
"""
def bin_search(arr, left, high, x):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]==x):
            return(mid)
        elif(arr[mid]>x):
            h=mid-1
        else:
            l=mid+1
    return -1
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        x=int(input())
        print (bin_search(arr, 0, 0, x))
