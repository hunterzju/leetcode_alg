'''
Description: file content
Author: hunterzju
Date: 2022-01-20 21:45:12
LastEditors: `${env:USERNAME}`
LastEditTime: 2022-01-25 22:43:37
FilePath: /leetcode_alg/leetcode/s45.py
'''
class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance: 
                if curDistance != len(nums) - 1:
                    ans += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1: break
        return ans