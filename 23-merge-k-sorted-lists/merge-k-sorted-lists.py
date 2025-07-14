# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Create a heap
        push all the head nodes from lists onto the min heap
        create a dummy node to indicate start of list. and a tail pointer
        then while the heap exists, pop from it the top node.
        make the tail.next point to that node
        tail = tail.next
        then for node.next (if exists) push back onto the heap.
        repeat while the heap exists
        '''
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



