'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        while '()' in s or '[]' in s or '{}' in s:
            if '()' in s:
                s = s.replace('()','')
            if '{}' in s:
                s = s.replace('{}','')
            if '[]' in s:
                s = s.replace('[]','')
                
        if s!='':
            return False
        else:
            return True



s=Solution()
print(s.isValid("([)]")) #False
print(s.isValid("(}")) #False
print(s.isValid("{[]}")) #True