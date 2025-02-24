import random

class Solution:

    def __init__(self, w: List[int]):
        """
        Build a prefix sum array of weights.
        prefixSums[i] = sum of w[0]..w[i].
        totalSum = sum of all weights.
        """
        self.prefixSums = []
        runningSum = 0
        for weight in w:
            runningSum += weight
            self.prefixSums.append(runningSum)
        self.totalSum = runningSum

    def pickIndex(self) -> int:
        """
        1. Generate a random float x in [0, totalSum).
        2. Linearly find which prefix interval x falls into.
        3. Return the index of that interval.
        """
        x = random.random() * self.totalSum  # random float in [0, totalSum)

        # Linear search: find the smallest i where prefixSums[i] > x
        for i, prefixVal in enumerate(self.prefixSums):
            if x < prefixVal:
                return i

        # Fallback (shouldn't normally happen if w has positive weights):
        return len(self.prefixSums) - 1
