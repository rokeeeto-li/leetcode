# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        if head.next == None: 
            return None
        for i in range(n):
            fast = fast.next
        if fast != None:
            while fast.next:
                fast = fast.next
                slow = slow.next
        else: 
            head = head.next
            return head
        slow.next = slow.next.next            
        return head
