class Solution:
    def twoSum(self, nums, target: int):
        hashmap = dict()
        for idx, num in enumerate(nums):
            hashmap[num] = idx 
        for idx, num in enumerate(nums):
            res_idx = hashmap.get(target-num)
            if res_idx != None and res_idx != idx:
                return [idx, res_idx]

if __name__ =="__main__":
    sol = Solution()
    test_nums = [3,3]
    test_tar = 6
    res = sol.twoSum(test_nums, test_tar)
    print(res)