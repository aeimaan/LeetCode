# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        l = head
        m = l.next
        r = m.next

        l.next = None
        m.next = l

        while r:
            tmp = r.next 
            r.next = m
            m = r 
            r = tmp
        
        
        return m
