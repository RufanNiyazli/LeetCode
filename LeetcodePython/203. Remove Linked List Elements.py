class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        dummy.next
