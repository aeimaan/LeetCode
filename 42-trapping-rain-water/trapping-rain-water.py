class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        res = 0

        for i in range(n):
            max_left[i] = max(height[i], max_left[i-1] if i >0  else 0)
        
        for i in range(n-1, -1, -1):
            max_right[i] = max(height[i], max_right[i+1] if i < n-1 else 0)

        for i in range(n):
            minn = min(max_left[i], max_right[i]) 
            if minn > height[i]:
                res += minn - height[i]
        return res    
        