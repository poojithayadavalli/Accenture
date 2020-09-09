"""
Given a number N, print the first N Fibonacci numbers.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains the integer N.

Output:
Print the first n fibonacci numbers with a space between each number. Print the answer for each test case in a new line.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1<= T <=100
1<= N <=84

Example:
Input:
2
7
5

Output:
1 1 2 3 5 8 13
1 1 2 3 5

Explanation: Some of the numbers of the Fibonacci numbers are 1, 1, 2, 3, 5, 8, 13 ..... (N stars from 1).
"""
def fibo(n):
    dp = [0 for i in range(n+3)]
    dp[1] = 1
    dp[2] = 1

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2] 

    print(*dp[1:n+1])
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        fibo(n)
