class Solution(object):
    def majorityElement(self, nums):
        nums=sorted(nums)
        nums.append(nums[0])
        print(nums)
        a=nums[0]
        b=1
        c=0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                c+=1
                
            else:
                c+=1
                if b<c:
                    a=nums[i]
                    b=c
                    c=0
                else:
                    c=0
        return a