class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # call an auxiliary function, an array allows us to pass information, by reference
		# auxiliary
        ans = [0]
		# sum values, the sum is keeped in the array
        self.inOrderSum(root,ans)
		# convert the tree
        return self.convertInOrder(root, ans)
		
    def convertInOrder(self, root, ans):
        """
        root: Tree Node
        ans [array] the first value has the current sum
        """
        # if the root is None, do Nothing
        if not root:
            return None
       #  inOrder, check first the left node 
        root.left = self.convertInOrder(root.left, ans)
        #save current value of the node
        tmp = root.val
        #assign new value
        root.val= ans[0]
        #substract the previous node value to our sum (ans)
        ans[0]+=-tmp
        #check the right node 
        root.right = self.convertInOrder(root.right, ans)
        return root
    
    def inOrderSum(self, root,ans):
        """ using array on python allows us to pass by rerefence
        root: Node Tree
        ans: array, the first element allows we keep the sum 
        """
        if not root:
            return True
        self.inOrderSum(root.left,ans)
        ans[0] += root.val
        self.inOrderSum(root.right,ans)
        return ans 
