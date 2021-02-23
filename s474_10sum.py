class Solution:
    def zeroAndOnes(self, cur_str: str):
        res = [0,0]
        for s in cur_str:
            if s == '0':
                res[0] += 1
            else:
                res[1] += 1
        return res

    def findMaxForm(self, strs, m: int, n: int) -> int:
        # dp_list is (m+1) x (n+1) matrix m->zero, n->one
        dp_list = []
        for i in range(0,m+1):
            dp_list.append([0 for j in range(0,n+1)])
        
        for _str in strs:
            res = self.zeroAndOnes(_str)
            print(res)
            for i in range(m, res[0]-1, -1):
                for j in range(n, res[1]-1, -1):
                    dp_list[i][j] = max((dp_list[i-res[0]][j-res[1]]+1), dp_list[i][j])
        
        return dp_list[m][n]

def test():
    str_list = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    sol = Solution()
    res = sol.findMaxForm(str_list, m, n)
    print(res)

if __name__ == "__main__":
    test()
