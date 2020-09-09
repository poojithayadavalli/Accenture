"""
You are given 2 numbers (N , M); the task is to find N√M (Nth root of M).
Constraints:
2 <= N <= 20
1 <= M <= 109+5

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. 
Each test case contains two space separated integers N and M.

Output:
For each test case, in a new line, print an integer denoting Nth root of M if the root is an integer else print -1.

Example:
Input:
2
2 9
3 9
Output:
3
-1
"""
import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    rt = m ** (1/n)
    fl = math.floor(rt)
    ce = math.ceil(rt)
    if m == fl**n:
        print(fl)
    elif m == ce**n:
        print(ce)
    else:
        print(-1)
