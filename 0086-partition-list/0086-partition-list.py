# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = []
        list1 = []
        list2 = []

        while head:
            l.append(head.val)
            head = head.next

        for i in l:
            if i < x:
                list1.append(i)
            else:
                list2.append(i)

        concat = list1 + list2
        
        dummy = ListNode(0)
        curr = dummy
        for val in concat:
            curr.next  = ListNode(val)
            curr = curr.next

        return dummy.next