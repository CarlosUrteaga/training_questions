class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new = head
        if not head:
            return head
        dictionary = {}
        i = 1
        while head:
            dictionary[i] = head
            head = head.next
            i+=1
        mx = i-1
        tmp_k = dictionary[k]
        tmp_n_k = dictionary[mx-k+1]
        tmp_k.val, tmp_n_k.val =  tmp_n_k.val, tmp_k.val
        return new
