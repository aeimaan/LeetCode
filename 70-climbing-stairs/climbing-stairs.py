class Solution:
    def climbStairs(self, n: int) -> int:
        state = [1] * (n+1)

        for i in range(n-2, -1, -1):
            state[i] = state[i + 1] + state[i+2]

        return state[0]