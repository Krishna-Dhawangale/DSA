# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        curr = head

        while curr.next:
            curr = curr.next
            length += 1
        
        k %= length
        if k == 0:
            return head

        curr.next = head
        steps = length - k
        new_curr = head

        for i in range(1, steps):
            new_curr = new_curr.next

        new_head = new_curr.next
        new_curr.next = None

        return new_head