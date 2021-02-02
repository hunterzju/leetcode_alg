class Solution:
    def numWays(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        elif n == 2:
            return 2
        else:
            return (self.numWays(n-1) + self.numWays(n-2)) % 1000000007

if __name__ == "__main__":
    sol = Solution()
    res = sol.numWays(100)
    print(res)