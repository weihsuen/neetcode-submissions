# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Find middle: Fast slow pointer
        slow = head #cannot be int!!
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Update: slow should be the start of the middle now

        #Reverse second
        cur = slow.next #second list starts at the node after slow
        prev = None
        
        
        while cur: #temp will be none before cur
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        #Merge
        slow.next = None
        list1 = head #rmb to break list into two, else list1 is still the entir elist
        list2 = prev #make sure to use the reversed list, prev holds it!!! not cur as cur is None
        #temp = head

        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2


        