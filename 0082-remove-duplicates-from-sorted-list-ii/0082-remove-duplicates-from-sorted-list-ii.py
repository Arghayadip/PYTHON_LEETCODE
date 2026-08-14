class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr is not None:
            if curr.next is not None and curr.val == curr.next.val:
                value = curr.val

                while curr is not None and curr.val == value:
                    curr = curr.next

                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next