# 复杂版
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        for val in g:
            match = False
            for num in s:
                if num >= val:
                    match = True
                    s.remove(num)
                    break
            if match:
                cnt += 1
        return cnt

# 简单版
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        cnt = 0
        idx = 0
        # 大饼干分给胃口大的小朋友
        for val in g:
            if (idx<len(s) and s[idx] >= val):
                cnt += 1
                idx -=1
        return cnt