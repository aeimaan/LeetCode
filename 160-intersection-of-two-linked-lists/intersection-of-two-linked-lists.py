# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        tmp= headA
        while tmp:
            seen.add(tmp)
            tmp = tmp.next
        
        tmp = headB
        while tmp:
            if tmp in seen:
                return tmp
            tmp= tmp.next
        
        return tmp