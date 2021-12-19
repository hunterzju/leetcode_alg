class Solution:
    def search(self, nums: list[int], target: int) -> int:
        max_idx = len(nums)
        min_idx = 0
        mid_idx = max_idx // 2

        while mid_idx != min_idx:
            if target == nums[mid_idx]:
                return mid_idx
            elif target > nums[mid_idx]:
                min_idx = mid_idx
                mid_idx = min_idx + (max_idx - min_idx) // 2
            else:
                max_idx = mid_idx
                mid_idx = max_idx // 2
        if target == nums[mid_idx]:
            return mid_idx
        else:
            return -1

if __name__ == "__main__":
    test1 = [-1, 0, 3, 5, 9, 12]    # target = 9
    sol = Solution()
    res = sol.search(test1, 9)
    print(res)