# Last updated: 22/04/2025 16:51:53
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3: List[int] = nums1 + nums2
        nums3.sort()
        if len(nums3)%2 == 1:
            return nums3[(len(nums3)-1)//2]
        else:
            n1 = nums3[len(nums3)//2]
            n2 = nums3[len(nums3)//2 - 1]
            res = (n1 + n2)/2
            return res