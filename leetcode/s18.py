class Solution:
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        nums_len = len(nums)
        for idx1 in range(nums_len-1):
            # 去重
            if idx1 > 0 and nums[idx1] == nums[idx1-1]:
                continue
            for idx2 in range(idx1+1, nums_len):
                # 去重
                if idx2 > idx1+1 and nums[idx2] == nums[idx2-1]:
                    continue

                left = idx2+1
                right = len(nums) - 1

                # 判断四数之和，中间做剪枝
                while left < right:
                    sum4 = nums[idx1] + nums[idx2] + nums[left] + nums[right]
                    if sum4 - target > 0:
                        while(left != right and nums[right]==nums[right-1]):
                            right -= 1
                        right -= 1
                    elif sum4 - target < 0 : 
                        while(left != right and nums[left]==nums[left+1]):
                            left += 1
                        left += 1
                    else:
                        res.append([nums[idx1], nums[idx2], nums[left], nums[right]])
                        while(left != right and nums[left]==nums[left+1]):
                            left += 1
                        while(right != left and nums[right]==nums[right-1]):
                            right -= 1
                        left += 1
                        right -= 1
        return res