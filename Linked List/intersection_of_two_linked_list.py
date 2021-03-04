# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
            
            if pointerA is None:
                pointerA = headB
            else:
                pointerA = pointerA.next
            if pointerB is None:
                pointerB = headA
            else:
                pointerB = pointerB.next
        return pointerA