# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head):
        new = ListNode(0)
        cur = head

        while cur:
            next_node = cur.next
            temp = new

            while temp.next and temp.next.val < cur.val:
                temp = temp.next

            cur.next = temp.next
            temp.next = cur
            cur = next_node

        return new.next
