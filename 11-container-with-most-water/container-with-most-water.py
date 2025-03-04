class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_vol = 0

        while l < r:
            vol = calc_volume(l,r, height[l], height[r])
            max_vol = max(max_vol, vol)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_vol

def calc_volume(x,y,h1, h2) -> int:
    return (y-x) * min(h1, h2)