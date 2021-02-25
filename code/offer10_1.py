class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.fib(n-1) + self.fib(n-2)) % 1000000007
    
    def fib_bp(self, n: int) -> int:
        a, b = 0,1
        for i in range(0, n):       # n-1次
            a, b = b, a+b 
        return a % 1000000007

if __name__ == "__main__":
    sol = Solution()
    print(sol.fib_bp(100))