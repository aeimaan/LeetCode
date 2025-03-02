class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lru, self.mru = Node(0, 0), Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.size = 0
    
    def updateNodeMRU(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.mru.prev
        self.mru.prev.next = node
        self.mru.prev = node
        node.next = self.mru
        return

    def get(self, key: int) -> int:
        if key in self.cache:
            # Switch this one to the MRU
            node = self.cache[key]
            self.updateNodeMRU(node)
            val = node.val
            return val
        return -1
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.updateNodeMRU(node)
        else:
            self.size += 1
            node = Node(key, value)
            self.cache[key] = node
            
            # Insert new node into LL
            node.prev = self.mru.prev
            self.mru.prev.next = node
            self.mru.prev = node
            node.next = self.mru
            # if self.size == 1:
            #     self.lru.next = node
        
            if self.size > self.cap:
                # evict the key at LRU
                node = self.lru.next
                keyToDel = node.key
                del self.cache[keyToDel]
                self.lru.next = node.next
                node.next.prev = self.lru
                node.prev = None
                node.next = None
                del node





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)