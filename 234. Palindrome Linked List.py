# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) space
    def isPalindrome(self, head):
        queue = collections.deque([])
        cur = head
        while cur:
            queue.append(cur)
            cur = cur.next
        while len(queue) >= 2:
            if queue.popleft().val != queue.pop().val:
                return False
        return True

class Solution:
    # O(1) space
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next