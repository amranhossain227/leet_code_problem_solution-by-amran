from git import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        p=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for k in range(i+1,len(nums)-2):
                if k>i+1 and nums[k]==nums[k-1]:
                    continue
                left=k+1
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[k]+nums[left]+nums[right]
                    if total==target:
                        l=[nums[i],nums[k],nums[left],nums[right]]
                        left=left+1
                        right=right-1
                        while(nums[left]==nums[left-1] and left<right):
                            left=left+1
                        while(nums[right]==nums[right+1] and left<right):
                            right=right-1
                        p.append(l)
                    elif total>target:
                        right=right-1
                    elif total<target:
                        left=left+1

            
        return p
        
k=Solution()
print(k.fourSum([2,2,2,2,2],8))