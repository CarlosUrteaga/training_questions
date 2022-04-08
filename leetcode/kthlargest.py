"""
keep k
and keep array
now we require to return the k element

"""

class Node:
    def __init__(self, val, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right

        class KthLargest:
        
    def insert_into_tree(self, val, head):
        if not head:
            return Node(val)
        elif val<head.val:
            head.left = self.insert_into_tree(val, head.left)
        else:
            head.right = self.insert_into_tree(val, head.right)
        return head

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.tree = None
        self.array = []
        for i in range(0,len(nums)):
            self.tree = self.insert_into_tree(nums[i], self.tree)
        # self.inOrder(self.tree, self.array)
        
    def inOrder (self, head, array):
        if head:
            if head.left:
                self.inOrder(head.left,array)
            array.append(head.val)
            if head.right:
                self.inOrder(head.right,array)
        

    def add(self, val: int) -> int:
        self.tree = self.insert_into_tree(val, self.tree)
        self.inOrder(self.tree, self.array)
        return self.array[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
