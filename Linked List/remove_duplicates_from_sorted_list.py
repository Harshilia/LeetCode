# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        output = pointer = ListNode(0)
        prev = None
        
        while head:
            
            if prev != head.val:
                pointer.next = ListNode(head.val)
                pointer = pointer.next
            prev = head.val
            head = head.next
        return output.next