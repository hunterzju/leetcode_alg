class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for idx, num in enumerate(nums):
            left = idx+1
            right = len(nums) - 1
            # nums[0] > 0, no sum = 0
            if num > 0:
                break
            # 去重
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            # 判断三数之和，中间做剪枝
            while left < right:
                sum3 = num + nums[left] + nums[right]
                if sum3 > 0:
                    while(left != right and nums[right]==nums[right-1]):
                        right -= 1
                    right -= 1
                elif sum3 < 0 : 
                    while(left != right and nums[left]==nums[left+1]):
                        left += 1
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    while(left != right and nums[left]==nums[left+1]):
                        left += 1
                    while(right != left and nums[right]==nums[right-1]):
                        right -= 1
                    left += 1
                    right -= 1
        return res
