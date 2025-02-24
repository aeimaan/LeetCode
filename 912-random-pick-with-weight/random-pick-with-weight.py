from random import randrange
class Solution:

    def __init__(self, w: List[int]):
       self.w = w
       self.sum = sum(w)
       self.p = [0] * len(w)
       soFar = 0
       for i in range(len(w)):
        x = w[i]
        curP = float(x/self.sum)
        soFar += curP
        self.p[i] = soFar



    def pickIndex(self) -> int:
        x = random.random()
        # for i in range(len(self.w)-1):
        #     if x > self.p[i] and x <= self.p[i+1]:
        #         return i+1
        lo = 0
        hi = len(self.p) - 1
        mid = 0
        while lo < hi:
            mid = (hi-lo)//2 + lo
            if self.p[mid] == x: return mid
            elif self.p[mid] < x: lo = mid + 1
            else: hi = mid 


        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()