class Solution:
    def numWays(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        elif n == 2:
            return 2
        else:
            return (self.numWays(n-1) + self.numWays(n-2)) % 1000000007

    '''
    jump 0: 1
    jump 1: 1
    jump 2: jump[0] + jump[1]
    '''
    def numWays_bp(self, n: int) -> int:
        if n <= 1:
            return 1
        bp_list = [-1 for i in range(0,n+1)]
        bp_list[0] = 1
        bp_list[1] = 1
        for i in range(2,n+1):
            bp_list[i] = (bp_list[i-1] + bp_list[i-2]) % 1000000007
        return bp_list[n]

if __name__ == "__main__":
    sol = Solution()
    res = sol.numWays_bp(2)
    print(res)