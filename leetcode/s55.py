class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if (nums[0] == 0):
            return False
        max_idx = 0             # 最大能访问到的位置
        max_len = len(nums)
        for idx, num in enumerate(nums):
            # 当前idx能被访问到，并且访问范围可以继续扩大，更新max_idx
            if (idx <= max_idx) and ((idx+num) > max_idx):
                max_idx = idx + num
        if max_idx >= max_len-1:
            return True
        else:
            return False