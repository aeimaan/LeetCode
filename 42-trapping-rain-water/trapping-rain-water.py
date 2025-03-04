class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        res = 0
        max_wall(height, max_left, 0, len(height))
        max_wall(height, max_right, len(height)-1, -1)
        for i in range(len(height)):
            minH = min(max_left[i], max_right[i])
            if height[i] < minH:
                res += minH - height[i]
        
        return res


def max_wall(height, arr, start, end):
    curMax = 0
    if start < end:
        for i in range(start, end):
            arr[i] = curMax
            curMax = max(curMax, height[i])
    else:
        for i in range(start, end, -1):
            arr[i] = curMax
            curMax = max(curMax, height[i])
    
        