from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        output = []
        q = deque()
        if root:
            q.append(root)
        while q:
            levels = []
            for _ in range(len(q)):
                node = q.popleft()
                levels.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            output.append(levels)
        return output