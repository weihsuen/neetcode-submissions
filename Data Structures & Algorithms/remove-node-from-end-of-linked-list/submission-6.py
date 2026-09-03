# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        index = 0 
        cur = head

        #find len of list
        while cur:
            index +=1
            cur = cur.next #here

        length = index
        index = 0
        cur = head

        if length == 1:
            return None
        elif n==length:
            head = head.next
            return head
        else:
            #get to node before n
            while index != (length - n -1):
                cur = cur.next #here2
                index +=1
            if n==1:
                cur.next = None
                return head
            else:
                cur.next = cur.next.next
                return head