# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        f1 = head.next
        f2 = head
        f3 = f1  

        while f1 and f1.next:
            f2.next = f1.next
            f2 = f2.next
            f1.next = f2.next
            f1 = f1.next
        

        f2.next = f3
        return head
