# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         arr=[]
#         arr1=[]
#         for i in range(0,m):
#             arr.append(nums1[i])
     
#         for i in range(0,n):
#             arr.append(nums2[i])
      
#         arr=sorted(arr)
#         for i in range(0,len(arr)):
#             if arr[i]!=0:
#                 arr1.append(arr[i])
#         return arr1
        

        
    
# k=Solution()
# print(k.merge([],0,[1],1))

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result=[]
        result1=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if(nums1[i]<nums2[j]):
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        for i in range(0,len(result)):
            if(result[i]!=0):
                result1.append(result[i])
        return result1
result=Solution()
result1=result.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(result1)

