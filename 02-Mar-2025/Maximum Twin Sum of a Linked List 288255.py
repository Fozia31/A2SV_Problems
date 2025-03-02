# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow , fast = head , head
        first_half = None

        while fast and fast.next:
            fast =fast.next.next
            temp = slow.next
            slow.next = first_half
            first_half = slow 
            slow = temp

        max_val = 0
        while slow:
            max_val = max(max_val , first_half.val + slow.val)
            first_half = first_half.next
            slow = slow.next

        return max_val

        