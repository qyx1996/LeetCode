class Solution:
    # This is my solution. But I think it's wrong since I
    # create new nodes, not using the originall l1 and l2 nodes
    def mergeTwoLists(self, l1, l2):
        root = n = ListNode(0)
        while l1 or l2:
            if not l1:
                n.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                n.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val >= l2.val:
                n.next = ListNode(l2.val)
                l2 = l2.next
            elif l1.val < l2.val:
                n.next = ListNode(l1.val)
                l1 = l1.next
            n = n.next
        return root.next
