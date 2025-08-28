class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    l=[nums[i],nums[left],nums[right]]
                    left=left+1
                    right=right-1
                    while(nums[left]==nums[left-1] and left<right):
                        left=left+1
                    while(nums[right]==nums[right+1] and left<right):
                        right=right-1
                    p.append(l)
                elif total>0:
                    right=right-1
                elif total<0:
                    left=left+1
        return p
                
