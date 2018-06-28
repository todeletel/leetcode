#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (35.68%)
# Total Accepted:    305.1K
# Total Submissions: 854.9K
# Testcase Example:  '-2147483648'
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
#
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction
# of using extra space.
#
# You could also try reversing an integer. However, if you have solved the
# problem "Reverse Integer", you know that the reversed integer might overflow.
# How would you handle such case?
#
# There is a more generic way of solving this problem.
#
#
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        tmp = str(abs(x))
        i , j = 0, len(tmp)-1
        while i < j:
            if tmp[i] != tmp[j]:
                return False
            i+=1
            j-=1
        return True
