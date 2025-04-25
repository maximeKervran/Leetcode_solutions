# Last updated: 25/04/2025 13:24:37
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #res = -1
        #for i in range(len(height)):
            #for j in range(i+1,len(height)):
                #h = min(height[i], height[j])
                #area = h * (j-i)
                #res = max(res, area)
        #return res
        
        res = -1
        left = 0
        right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res