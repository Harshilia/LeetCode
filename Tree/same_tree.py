# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # if p and q:
        #     return p.val==q.val and self.isSameTree(p.left,q.left)and self.isSameTree(p.right,q.right)
        # else:
        #     return p==q
        
        stack = [(p,q)]
        while stack:
            node1,node2 = stack.pop()
            
            if node1 and node2 and node1.val == node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            elif not node1 and not node2:
                continue
            else:
                return False
        return True
        
        