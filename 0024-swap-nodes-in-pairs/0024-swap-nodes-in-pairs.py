# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next is not None and prev.next.next is not None:
            fast = prev.next
            second = fast.next

            fast.next = second.next
            second.next = fast
            prev.next = second

            prev = fast
        return dummy.next

