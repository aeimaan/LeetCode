"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        if not head:
            return head

        tmp = head
        while tmp:
            hashmap[tmp] = Node(tmp.val)
            tmp = tmp.next

        tmp = head
        while tmp:
            if tmp.next: hashmap[tmp].next = hashmap[tmp.next]
            if tmp.random: hashmap[tmp].random = hashmap[tmp.random]
            tmp = tmp.next

        return hashmap[head]   