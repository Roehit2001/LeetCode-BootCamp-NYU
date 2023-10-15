class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        value_grid = {}
        u=""
        for idx in range(len(s)):
            if s[idx] in value_grid:
                u += value_grid[s[idx]]
            else:
                if t[idx] in value_grid.values():
                    return False
                else:
                    value_grid[s[idx]] = t[idx]
                    u = u + value_grid[s[idx]]
          
            if u != t[0:idx+1]:
                return False
        
        if u == t:
            return True