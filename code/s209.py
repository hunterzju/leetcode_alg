# 该解法在数据量大的时候会超出时间限制；
class SolutionERR:
    def minSubArrayLen(self, target, nums) -> int:
        nums_len = len(nums)
        min_cnt = 10 ** 6
        for out_idx in range(0, nums_len):
            tmp_sum = 0
            num_cnt = 0
            for in_idx in range(out_idx, nums_len):
                tmp_sum += nums[in_idx]
                num_cnt += 1
                if tmp_sum >= target:
                    if num_cnt < min_cnt:
                        min_cnt = num_cnt
                    break
            # if tmp_sum >= target:
            #     if num_cnt < min_cnt:
            #         min_cnt = num_cnt
        if min_cnt < 10 ** 6:
            return min_cnt
        else:
            return 0

# 使用快慢指针构建滑动窗口
class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        nums_len = len(nums)
        fast_p, slow_p = 0, 0
        min_cnt = 10 ** 6

        tmp_sum = 0
        for fast_p in range(0, nums_len):
            tmp_sum += nums[fast_p]
            fast_p += 1
            while tmp_sum >= target:
                tmp_len = fast_p - slow_p
                if tmp_len < min_cnt:
                    min_cnt = tmp_len
                tmp_sum -= nums[slow_p]
                slow_p += 1

        if min_cnt < 10 ** 6:
            return min_cnt
        else:
            return 0

if __name__ == "__main__":
    sol = Solution()
    test_nums1 = [1, 1,1,1,1,1]
    target1 = 11
    test_nums2 = [2,3,1,2,4,3]
    target2 = 7 
    target3 = 15
    test_nums3 = [5,1,3,5,10,7,4,9,2,8]
    res = sol.minSubArrayLen(target1, test_nums1)
    print(res)
