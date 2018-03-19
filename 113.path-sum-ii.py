#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (35.47%)
# Total Accepted:    158.6K
# Total Submissions: 447.2K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# 
# For example:
# Given the below binary tree and sum = 22,
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
# 
# 
# 
# return
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution(object):
    result = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result=[]
        ctx = []
        self.ctx_sum(root, sum, ctx)
        return self.result

    def ctx_sum(self, root, sum, ctx):
        if root is None:
            return False
        new = copy.copy(ctx)
        new.append(root.val)
        if root.left is None and root.right is None:
            if root.val == sum:
                self.result.append(new)
                return True
            else:
                return False
        return self.ctx_sum(root.left, sum-root.val, new) + self.ctx_sum(root.right, sum-root.val, new)



