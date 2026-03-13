# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # not very time efficient, but memory efficient
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    
    def hasCycleTimeTell(self, head: Optional[ListNode]) -> bool: # can tell exactly when the loop happened. Has to allocate set
        _set = set()
        cur = head

        while cur:
            if cur in _set:
                return True

            _set.add(cur)
            cur = cur.next

        return False