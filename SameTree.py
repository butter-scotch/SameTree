class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSameTree(self, p, q):

    if not p and not q:
      return True
    if not p or not q:
      return False
    if p.val != q.val:
      return False
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

result1 = TreeNode([1,2,1])
result2 = TreeNode([1,1,2])

result = Solution()
print(result.isSameTree(result1, result2))

