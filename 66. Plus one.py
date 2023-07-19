'''
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

class Solution:
    def plusOne(self, digits):
        new=int(''.join([map(str,digits)]))
        neww=new+1
        listt=[]
        for i in str(neww):
            listt.append(i)
        return listt
s=Solution()
print(s.plusOne([1,2,3]))