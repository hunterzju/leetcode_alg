# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def subtree_sum(root:TreeNode) -> int:
    if root.left == None and root.right == None:
        return root.val
    elif root.left == None and root.right != None:
        return root.val + subtree_sum(root.right)
    elif root.left != None and root.right == None:
        return root.val + subtree_sum(root.left)
    else:
        return root.val + subtree_sum(root.left) + subtree_sum(root.right)

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
            return 0
        elif root.left == None and root.right != None:
            return subtree_sum(root.right) + self.findTilt(root.right)
        elif root.left != None and root.right == None:
            return subtree_sum(root.left) + self.findTilt(root.left)
        else:
            return abs(subtree_sum(root.left) - subtree_sum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)