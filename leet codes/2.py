# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''
        
        while l1 or l2:
            if l1:
                n1 += str(l1.val)
                l1 = l1.next
            else:
                n1 += '0'

            if l2:
                n2 += str(l2.val)
                l2 = l2.next
            else:
                n2 += '0'

        n1 = int(n1[::-1])
        n2 = int(n2[::-1])

        result = str(n1 + n2)
        
        newList = ListNode()
        tail = newList

        for i in result[::-1]:
            tail.next = ListNode(int(i))
            tail = tail.next

        return newList.next
