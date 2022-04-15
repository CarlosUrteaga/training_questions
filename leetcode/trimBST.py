class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # if we have a empty root we will return return None 
        if not root:
            return root
		# if my current value is equal to high I known that the right has greather values so, i can prune(to none)
        if root.val == high:
            root.right = None
		# if my current value is equal to low, I known that the left has lower values so, i can prune(to none)
        if root.val ==low:
            root.left = None
		# if my current value is lower than my low, so i will replaced with high values, check right we can null left
        if root.val< low:
            root = self.trimBST(root.right, low, high)
		# if my current value is greather than my high , so i will replaced with lower values, prune to left null right
        if high <root.val:
            root = self.trimBST(root.left, low, high)
		# if we steel have a root, check the childs
		if root:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        
        return root
