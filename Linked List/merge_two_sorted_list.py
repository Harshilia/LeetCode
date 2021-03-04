# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        output = pointer = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1= l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        if l1 or l2:
            pointer.next = l1 or l2
        
        return output.next
    


