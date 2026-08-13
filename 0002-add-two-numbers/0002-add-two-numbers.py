# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1 is not None:
                x = l1.val
            else: 
                x = 0
            if l2 is not None:
                y = l2.val
            else: 
                y = 0
            total = x+y+carry

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next
