# 暴力求解，复杂度太高
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -2**63
        for outer_idx, outer_val in enumerate(nums):
            tmp_sum = 0
            for inner_val in nums[outer_idx:]:
                tmp_sum += inner_val
                if tmp_sum > max_sum:
                    max_sum = tmp_sum
        return max_sum

# 贪心法
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -2**63
        cur_sum = 0
        for val in nums:
            cur_sum += val
            if (cur_sum > max_sum):
                max_sum = cur_sum
            # cur_sum为负数的时候打破局部最优，重新计算
            if (cur_sum <= 0):      
                cur_sum = 0
        return max_sum
