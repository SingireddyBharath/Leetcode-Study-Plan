class Solution:
    def largestPerimeter(self, nums: List[int]) -> int: 
        nums.sort()
        res=0    
        i,j=0,2
        while j<len(nums):
            a=nums[i]
            b=nums[i+1]
            c=nums[i+2]             
            if a+b>c and b+c>a and a+c>b:
                res=max(res,a+b+c)
            i+=1
            j+=1 
            
        return res
