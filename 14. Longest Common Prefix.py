'''
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs):
        min_length=0
        min_len=min(len(i) for i in strs)
        for w in strs:
            w = w[:min_len]
            
        if len[i] < len[i+1] :
            max_length = len[i+1]
        else:
            max_length = len[i]
            
        for j in range(max_length):
            if i[j] == strs[j][j]:
                continue
        return ''


s=Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
      