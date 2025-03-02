# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seena = set()
        seenb = set()

        tmpa= headA
        tmpb = headB

        while tmpa or tmpb:
            seena.add(tmpa)
            seenb.add(tmpb)
            if tmpa in seenb:
                return tmpa
            if tmpb in seena:
                return tmpb
            if tmpa: tmpa = tmpa.next
            if tmpb: tmpb = tmpb.next
        
        return tmpb