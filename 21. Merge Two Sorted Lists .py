class Solution:
# This is my modified solution. This time original nodes are used
    def mergeTwoLists(self, l1, l2):
        root = n = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                n.next = l2
                l2 = l2.next
            else:
                n.next = l1
                l1 = l1.next
            n = n.next
        if not l1:
            n.next = l2
        if not l2:
            n.next = l1
        return root.next

class Solution:
    # This is my original solution. But I think it's wrong since I
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
