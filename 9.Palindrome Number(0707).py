'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''

class Solution:
    def isPalindrome(self,x):
        x_str=str(x)
        if len(x_str) == 1:
            return True
        for i in range(len(x_str)//2):
            if x_str[i] == x_str[i-1]:
                return True
            elif len(x_str) == 1 or x_str[i] != x_str[i-1]:
                return False

        
            

s=Solution()
print(s.isPalindrome()) #True
print(s.isPalindrome(10)) #False