
## solution 1
class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        sub_list = [nums[idx]-nums[idx+1] for idx in range(0, len(nums)-1)]
        sig = -1 if sub_list[0] > 0 else 1
        for val in sub_list:
            if val != 0:
                sig = -1 if val > 0 else 1
                break
        res = 1
        for val in sub_list:
            if sig * val < 0:
                res += 1
                sig *= -1
            else:
                continue
        return res 

# solution 2
class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        pre_diff = 0
        cur_diff = 0
        res = 1
        for idx in range(0,len(nums)-1):
            cur_diff = nums[idx+1] - nums[idx]
            if (cur_diff > 0 and pre_diff<=0) or (cur_diff <0 and pre_diff >=0):
                res += 1
                pre_diff = cur_diff
        return res