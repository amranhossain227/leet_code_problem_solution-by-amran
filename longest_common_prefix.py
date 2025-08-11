class Solution(object):
    def longestCommonPrefix(self, strs):
        a=sorted(strs)
        str1=a[0]
        str2=a[-1]
        sum=0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                sum += 1
            else:
                break
        if sum == 0:
            return ""
        else:
            a = str1[:sum]
        return a
    
    
result=Solution()
print(result.longestCommonPrefix(["flower","flow","flight"]))
