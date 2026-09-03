# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        myMap = {}
        cur = head 
        index = 0


        while cur:
            myMap[index] = cur
            cur = cur.next
            index +=1

        if len(myMap) == 1:
            return None

        if len(myMap) == n:
            head = head.next
            return head

        if n == 1:
            myMap[len(myMap) -n -1 ].next = None
            return head

        myMap[len(myMap) - n -1].next = myMap[len(myMap) -n +1]

        return head

        