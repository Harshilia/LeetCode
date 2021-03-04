# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Traverse until middle of the linkedlist
        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the lower half of linkedlist
        slow = self.reverse_ll(slow)
        fast = head
        
        # Compare values of upper half and lower half of linkedlist
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
                
    # function for reversing the linkedlist
    def reverse_ll(self,slow):

        prev = None
        while slow:
            temp = slow.next 
            slow.next = prev
            prev = slow
            slow = temp
        return prev