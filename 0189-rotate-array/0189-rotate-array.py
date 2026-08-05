class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        x=nums[0:n-k]
        y=nums[n-k:n]
        nums[:]=y+x
        return nums