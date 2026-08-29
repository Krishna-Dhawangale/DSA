# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head and not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_ll = slow.next
        slow.next = None

        prev = None
        curr = second_ll

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first_ll = head
        second_ll = prev

        while second_ll:
            left = first_ll.next
            right = second_ll.next

            first_ll.next = second_ll
            second_ll.next = left

            first_ll = left
            second_ll = right