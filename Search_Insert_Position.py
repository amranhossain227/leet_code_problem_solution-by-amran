class Solution(object):
    def searchInsert(self, nums, target):
        left=0
        right=len(nums)-1
        middle=-1
       
        while(left<=right):
            middle=(left+right)//2
            if(nums[middle]==target):
                return middle
            elif(nums[middle]>target):
                right=middle-1
            else:
                left=middle+1
        if middle != -1:
            if nums[middle] < target:
                return middle + 1
            else:
                return middle
            return middle+1
result=Solution()
print(result.searchInsert([1,3,5,6], 7))  # Output: 4
print(result.searchInsert([1,3,5,6], 5))  # Output: 2
print(result.searchInsert([1,3,5,6], 2))  # Output: 1
print(result.searchInsert([1,3,5,6], 0))  # Output: 0
