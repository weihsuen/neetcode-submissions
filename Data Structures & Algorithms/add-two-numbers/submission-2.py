# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1head = l1
        l2head = l2
        ans = ListNode(0,None)
        carry = 0
        cur = ans

        while l1head or l2head or carry:
            l1val = l1head.val if l1head else 0
            l2val = l2head.val if l2head else 0

            sum = l1val + l2val + carry
            carry = sum // 10
            last = sum%10

            cur.next = ListNode(last, None)
            cur = cur.next

            l1head = l1head.next if l1head else None
            l2head = l2head.next if l2head else None

        return ans.next
            