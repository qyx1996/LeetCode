# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            root1.val += root2.val
            self.mergeTrees(root1.left, root2.left)
            self.mergeTrees(root1.right, root2.right)
            root1.left = root1.left if root1.left else root2.left
            root1.right = root1.right if root1.right else root2.right
        elif root1:
            return root1
        elif root2:
            root1 = root2
        else:
            return None
        return root1

    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans
