#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.39%)
# Total Accepted:    373.6K
# Total Submissions: 1.5M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# Input: 123
# Output:  321
# 
# 
# 
# Example 2:
# 
# Input: -123
# Output: -321
# 
# 
# 
# Example 3:
# 
# Input: 120
# Output: 21
# 
# 
# 
# Note:
# Assume we are dealing with an environment which could only hold integers
# within the 32-bit signed integer range. For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483647 or x < -2147483648:
            return 0
        nage = False
        if x < 0:
            nage = True
        temp = str(abs(x))
        new = 0
        for i in range(len(temp)):
            new = new + int(temp[i:i+1]) * 10**i

        new = new * -1 if nage else new
        if new > 2147483647 or new < -2147483648:
            return 0
        return new
