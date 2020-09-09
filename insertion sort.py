"""
Given a array A of size N. The task is to write the insert() function which is used to implement Insertion Sort.
Constraints:
1 <= N <= 1000
1 <= arr[i] <= 1000

Example 1:

Input:
5
4 1 3 9 7
Output: 
1 3 4 7 9
Example 2:

Input:
10 
10 9 8 7 6 5 4 3 2 1
Output: 1 2 3 4 5 6 7 8 9 10


"""
n=int(input())
x=list(map(int,input().split()))
x.sort()
print(*x)
