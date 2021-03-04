from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        # BFS approach
        
        q1 = deque([t1])
        q2 = deque([t2])
        while q1 and q2:
            node1, node2 = q1.popleft(), q2.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)                
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
        return t1
    
        ## Recursive approach
        if t1 and t2:
            answer = TreeNode(t1.val + t2.val)
            answer.left = self.mergeTrees(t1.left, t2.left)
            answer.right = self.mergeTrees(t1.right, t2.right)
            return answer

        else:
            return t1 or t2
        
            