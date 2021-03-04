# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

       if not lists:
            return
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left,right)


    def merge(self, left, right):
        merged_list = ListNode(0)
        pointer = merged_list

        while left and right:
            if left.val<= right.val:
                pointer.next = left
                left = left.next
            else:
                pointer.next = right
                right = right.next
            pointer = pointer.next

        if left or right:
            pointer.next = left or right

        return merged_list.next
        