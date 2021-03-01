class Solution:
    def pathSum(self, root, sum):
        if not root: return 0
        root_equal_sum = 1 if root.val == sum else 0
        return self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum) + \
               self.pathFromRootSum(root.left, sum - root.val) + \
               self.pathFromRootSum(root.right, sum - root.val) + \
               root_equal_sum
    def pathFromRootSum(self, root, sum):
        if not root: return 0
        root_equal_sum = 1 if root.val == sum else 0
        return self.pathFromRootSum(root.left, sum - root.val) + \
               self.pathFromRootSum(root.right, sum - root.val) + \
               root_equal_sum
