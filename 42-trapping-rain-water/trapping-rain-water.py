class Solution:



    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        water = 0

        max_wall(height, max_left, 0, len(height))
        max_wall(height, max_right, len(height)-1, 0)

        for i in range(len(height)):
            cur_height = height[i]
            min_wall = min(max_left[i], max_right[i])
            if cur_height >= min_wall:      ## cannot trap anything
                continue
            
            water += (min_wall - cur_height)
    
        return water

def max_wall(height, arr, start, end):
        max_before = 0
        if start<end:
            for i in range(start, end):
                arr[i] = max_before
                max_before = max(max_before, height[i])
        else:
           for i in range(start, end, -1):
                arr[i] = max_before
                max_before = max(max_before, height[i]) 


    