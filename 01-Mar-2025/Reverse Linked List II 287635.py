# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        next_node = None
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp
        
        prev.next.next = curr
        prev.next = next_node
        
        return dummy.next

        