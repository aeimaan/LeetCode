class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for idx, maxJump in enumerate(nums):
            if furthest < idx: 
                return False
            furthest = max(furthest, idx + maxJump)

        return True
            