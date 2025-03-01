class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.size = 0
        self.l = 0
        self.r = 0
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.size >= self.cap:
            return False
        self.q[self.r] = value
        self.size += 1
        self.r += 1
        self.r = self.r % self.cap
        return True

    def deQueue(self) -> bool:
        if self.size == 0: return False
        self.l += 1 
        self.l = self.l % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0: return -1
        return self.q[self.l]

    def Rear(self) -> int:
        if self.size == 0: return -1
        if self.r - 1 < 0:
            return self.q[-1]
        return self.q[self.r - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()