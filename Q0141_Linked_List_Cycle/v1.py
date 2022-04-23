# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dics = set()
        while head is not None:
            if head in dics:
                return True
            else:
                dics.add(head)
                head = head.next
        return False
