# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = head
        length = 1
        now = head
        dummy = head
        cur = head
        while l:
            l = l.next
            length += 1
        if length % 2 != 0:
            return False
        iteration = length / 2

        while cur:
            for _ in range(iteration):
                now = now.next

            if now.val != cur.val:
                return False
            
            
            length += 1
            if length > iteration:
                break
        return True
