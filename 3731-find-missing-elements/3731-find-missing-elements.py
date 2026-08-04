class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        min1=nums[0]
        max1=nums[-1]
        a=[]
        for i in range(min1,max1):
            a.append(i)
        b=list(set(a)-set(nums))
        b.sort()
        return b

