# code
# Given an array A of size N, print second largest element from an array.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# T testcases follow. Each testcase contains two lines of input.
# The first line contains an integer N denoting the size of the array.
# The second line contains the N space seperated intgers of the array#
n = int(input())
for i in range(n):
    t = int(input())
    a = [a for a in map(int, input().rstrip().split(" "))]
    lar = 0
    second = 0
    for r in range(len(a)):
        if a[r] >= lar:
            second = lar
            lar = a[r]
        elif a[r] >= second:
            second = a[r]
    print(second)
