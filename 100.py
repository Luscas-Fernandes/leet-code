# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preOrder(node):
            if node is None:
                return [None]
            
            visited = [node.val]
            visited = visited + preOrder(node.left)
            visited = visited + preOrder(node.right)
            
            return visited

        nodesP = preOrder(p)
        nodesQ = preOrder(q)

        if nodesP == nodesQ:
            return True

        return False
    