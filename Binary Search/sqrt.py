"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example:
Input: x = 4
Output: 2


Example:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

def mySqrt(x):
    if x <= 1:
        return x
    left, right = 1, x // 2
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        temp = mid * mid
        if temp == x:
            return mid
        elif temp < x:
            ans = mid
            left = mid + 1
        elif temp > x:
            right = mid - 1
    return ans


print(mySqrt(8))