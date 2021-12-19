class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = dict()
        for ch in magazine:
            if ch in mag_map.keys():
                mag_map[ch] += 1
            else:
                mag_map[ch] = 1
        
        for ch in ransomNote:
            if ch in mag_map.keys():
                if mag_map[ch] > 0:
                    mag_map[ch] -= 1
                else:
                    return False
            else:
                return False
        return True