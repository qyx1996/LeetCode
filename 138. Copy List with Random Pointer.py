class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        m, m[None], n = collections.defaultdict(lambda: Node(0, None, None)), None, head
        while n:
            m[n].val, m[n].next, m[n].random, n = n.val, m[n.next], m[n.random], n.next
        return m[head]