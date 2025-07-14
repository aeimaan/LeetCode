import random
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.map: return False
        self.list.append(val)
        self.map[val] = self.size
        self.size +=1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        self.size -= 1
        idx = self.map[val]
        lastVal = self.list[-1]
        self.list[-1], self.list[idx] = self.list[idx], self.list[-1]
        del self.list[-1]
        del self.map[val]

        if idx != self.size: self.map[lastVal] = idx

        return True

    def getRandom(self) -> int:
        r = random.randint(0, self.size-1)
        return self.list[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()