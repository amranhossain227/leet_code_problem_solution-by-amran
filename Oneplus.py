class Solution(object):
    def plusOne(self, digits):
        string=""
       
        for i in range(0,len(digits)):
            string+=str(digits[i])
        a=int(string)+1
        string=str(a)
        result=[]
        for i in range(0,len(string)):
            result.append(int(string[i]))
        # or
        # result=[int(C) for C in string]
        return result