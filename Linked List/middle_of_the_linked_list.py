# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def middleNode(self, head: ListNode) -> ListNode:

        ## Efficient solution
        first = second = head
        while second and second.next:
            first = first.next
            second = second.next.next
        return first

#         node = head
#         count = 0
#         while head is not None:
#             count+=1
#             head = head.next
#         if count%2 == 0 :
#             index = (count/2)
#         else:
#             index = count//2

#         temp = 0
#         while True:
#             if temp<index:
#                 node = node.next
#             else:break
#             temp += 1
#         return node
