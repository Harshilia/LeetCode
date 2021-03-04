# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ## Iterative
        # if root is None:
        #     return None
        # q = [root]
        # depth = 0
        # while q:
        #     depth += 1
        #     level = []
        #     for each in q:
        #         if each.left:
        #             level.append(each.left)
        #         if each.right:
        #             level.append(each.right)
        #     q = level
        # return depth
    
        ## Recursion
        if root==None:return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        