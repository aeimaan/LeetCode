# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = ""
        tmp = l1
        while tmp: 
            num1 += str(tmp.val)
            tmp = tmp.next
        tmp = l2
        while tmp: 
            num2 += str(tmp.val)
            tmp = tmp.next
        x = num1[::-1] 
        y = num2[::-1]
        res = str(int(x)+ int(y))[::-1]
        dummy = ListNode()
        tmp = dummy
        for s in res:
            tmp.next = ListNode(int(s))
            tmp = tmp.next
        return dummy.next
