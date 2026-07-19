from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        y=nums1+nums2
        y.sort()
        n=len(y)
        if n%2==0:
            return (y[n//2]+y[(n//2)-1]) / 2
        else:
            return y[n//2]