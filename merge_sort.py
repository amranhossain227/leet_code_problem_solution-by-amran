class merge_sort_solution:
    def merge_divided(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=self.merge_divided(arr[:mid])
        right=self.merge_divided(arr[mid:])
        return self.merge(left,right)
    
    
    def merge(self,left,right):
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
result=merge_sort_solution()

print(result.merge_divided([2,4,2,9,1,4,7,3,2,9]))
        