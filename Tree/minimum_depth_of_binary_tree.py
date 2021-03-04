# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # if root is None:
        #     return 0
        # else:
        #     if root.left is None:
        #         return self.minDepth(root.right) + 1
        #     elif root.right is None:
        #         return self.minDepth(root.left) + 1
        #     else:
        #         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        
        # Using bfs
        if root is None:
            return 0
        q,level = collections.deque([(root,1)]), 0
        
        while q:
            node,level = q.popleft()
            if node.left is None and node.right is None:
                return level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        