# Last updated: 22/04/2025 16:47:45
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res: List[int] = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
