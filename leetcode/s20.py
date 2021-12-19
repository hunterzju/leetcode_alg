class Solution:
    def removeDuplicates(self, nums) -> int:
        nums_len = len(nums)
        if nums_len <= 1:
            return nums_len
        else:
            ''' fast pointer cur_idx, slow pointer idx '''
            cur_idx = 0
            cur_val = nums[0]
            for idx in range(1, nums_len):
                if nums[idx] == cur_val:
                    continue
                else:
                    cur_idx += 1
                    cur_val = nums[idx]
                    nums[cur_idx] = cur_val
            return cur_idx+1

if __name__ == "__main__":
    sol = Solution()
    res = sol.removeDuplicates([1,1,2,2])
    print(res)