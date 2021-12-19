class Solution:
    def getSum(self, n):
        tmp_sum = 0
        while n > 0:
            tmp_sum += (n % 10)**2
            n = n // 10
        return tmp_sum

    def isHappy(self, n: int) -> bool:
        res_set = set()
        while True:
            if n == 1:
                return True
            elif n in res_set:
                return False
            else:
                res_set.add(n)
                n = self.getSum(n)

if __name__ == "__main__":
    sol = Solution()

    res = sol.isHappy(10)
    print(res)