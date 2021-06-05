class Solution:
    def generateMatrix(self, n: int):
        maxtrix_res = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        val = 1
        while left <= right and up <= down:
            # left -> right
            for idx in range(left, right+1):
                maxtrix_res[up][idx] = val
                val += 1
            up += 1
            # up -> down
            for idx in range(up, down+1):
                maxtrix_res[idx][right] = val
                val += 1
            right -= 1
            # right -> left
            for idx in range(right, left-1, -1):
                maxtrix_res[down][idx] = val
                val += 1
            down -= 1
            # down -> up
            for idx in range(down, up-1, -1):
                maxtrix_res[idx][left] = val
                val += 1
            left += 1
        return maxtrix_res

if __name__ == "__main__":
    sol = Solution()
    res = sol.generateMatrix(4)
    print(res)