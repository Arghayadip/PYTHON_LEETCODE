class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        # Find middle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # For odd length, skip the middle node
        if fast is not None:
            slow = slow.next

        # Reverse second half
        prev = None

        while slow is not None:
            front = slow.next
            slow.next = prev
            prev = slow
            slow = front

        # Compare both halves
        left = head
        right = prev

        while right is not None:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True