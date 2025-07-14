# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for head in lists:
            if head:
                heappush(heap, (head.val, id(head), head))
        
        dummy = ListNode()
        tail = dummy
        while heap:
            val, addy, node = heappop(heap)
            tail.next = node
            tail = tail.next
            node = node.next
            if node: heappush(heap, (node.val, id(node), node))
        return dummy.next



