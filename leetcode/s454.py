class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        sum_map_ab = dict()     # key = sum, val = cnt
        for val1 in nums1:
            for val2 in nums2:
                sum = val1 + val2
                if sum in sum_map_ab.keys():
                    sum_map_ab[sum] += 1
                else:
                    sum_map_ab[sum] = 1
        # a,b,c,d sum = 0 count
        res_cnt = 0
        for val3 in nums3:
            for val4 in nums4:
                sum = -(val3 + val4)
                if sum in sum_map_ab.keys():
                    res_cnt += sum_map_ab[sum]
        
        return res_cnt

if __name__ == "__main__":
    sol = Solution()
    
