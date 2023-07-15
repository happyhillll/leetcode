'''
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
#이건 너무 어려븜
class Solution:
    def longestCommonPrefix(self, strs):
        min_len=0
        if len(strs) == 0:
            return ""
        for w in strs: #단어 하나
            min_len=min(len(w) for w in strs) #단어 중에 제일 짧은 단어의 길이
            for i in range(min_len-1): #가장 짧은 단어의 길이만큼 돌건데,
                for word in strs[1:]: #첫번째 단어를 제외한 나머지 단어들을 돌면서
                    if (strs[0][i] != word[i] or i == min_len-1): #첫번째 단어의 i번째 글자와 나머지 단어들의 i번째 글자가 다르거나, i가 min_len-1이면
                        return strs[0][:i] #루프를 멈추고, 첫번째 단어의 0번째부터 i-1번째까지를 리턴
        
        return ""          
        
        
s=Solution()
print(s.longestCommonPrefix(["ab","a"]))

#수정본
class Solution:
    def longestCommonPrefix(self, strs):
        ans =""
        min_len=min([len])
        for i in range(min_len):
            chars=[x[i] for x in strs]
            if len(set(chars))==1:
                ans += strs[0][i]
            else:
                break