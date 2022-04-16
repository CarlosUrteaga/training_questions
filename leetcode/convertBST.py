class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # call an auxiliary function, an array allows us to pass information, because is by reference
        return self.preOrder_inversed(root,[0])
        
    def preOrder_inversed(self, root,arr):
        # if the root is None return a none and no change in the array
        if not root:
            return None
        # pre order inversed, we will check first the rightest number
        root.right = self.preOrder_inversed(root.right,arr)
        # add to the value 
        # add the current carry and next 
        
        root.val+= arr[0]
        # change the new carry
        arr[0] = root.val
        # the same for the other side
        root.left = self.preOrder_inversed(root.left,arr)
        return root
