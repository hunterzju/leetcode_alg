class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        else:
            x = self.kthGrammar(N-1, (K+1)//2)
            if x == 0:
                if K % 2 == 0:
                    return 1
                else:
                    return 0
            else:
                if K % 2 == 0:
                    return 0
                else:
                    return 1

'''
优雅的写法
'''
class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1: return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)/2)


if __name__ == "__main__":
    sol = Solution()
    res = sol.kthGrammar(4,5)
    print(res)
