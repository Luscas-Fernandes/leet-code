# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        ahead = head
        cur = head

        if not head:
            return None

        while ahead and ahead.next:
            ahead = ahead.next.next
            cur = cur.next

        return cur # this solution is clever, love the logic