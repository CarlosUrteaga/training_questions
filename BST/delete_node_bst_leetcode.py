# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val >key:
            root.left = self.deleteNode(root.left, key)
        elif root.val <key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.right == None:
                if root.left == None:
                    root = None
                else:
                    root = root.left
            else:
                if root.left == None:
                    root = root.right
                else:
                    iop = self.inOrderPredecesor(root)
                    self.deleteNode(root, iop)
                    root.val = iop

        return root
            
            
    def inOrderPredecesor(self, root):
        root = root.left
        while root.right!= None:
            root = root.right
        return root.val
            
        