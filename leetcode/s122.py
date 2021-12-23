'''
Description: file content
Author: hunterzju
Date: 2021-12-23 21:57:44
LastEditors: `${env:USERNAME}`
LastEditTime: 2021-12-23 22:02:53
FilePath: /leetcode_alg/leetcode/s122.py
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        benefit = 0
        for idx in range(0, len(prices)-1):
            diff = prices[idx+1] - prices[idx]
            if diff >= 0:
                benefit += diff
        return benefit
