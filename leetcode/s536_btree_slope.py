# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def subtree_sum(root:TreeNode) -> int:
    if root == None:
        return 0
    else:
        return root.val + subtree_sum(root.left) + subtree_sum(root.right)

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return abs(subtree_sum(root.left) - subtree_sum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)