import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        dictionary = collections.defaultdict(list)
        q = collections.deque([(root,0,0)])
        
        while q:
            node,level,parent = q.popleft()
            dictionary[node.val] = [level,parent]
            if node.left:
                q.append((node.left, level+1, node.val))
            if node.right:
                q.append((node.right, level+1, node.val))
                
        if dictionary[x][0] == dictionary[y][0] and dictionary[x][1] != dictionary[y][1]:
            return True
        return False
            