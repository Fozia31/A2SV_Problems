# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        queue = deque([root])
        level = 0
        
        while queue:
            n = len(queue)
            if level % 2 == 0:
                prev_val = float('-inf')
            else:
                prev_val = float('inf')
            
            for _ in range(n):
                node = queue.popleft()
                val = node.val
                
                if level % 2 == 0 and val % 2 == 0:
                    return False
                if level % 2 == 1 and val % 2 != 0:
                    return False
                
                if level % 2 == 0 and val <= prev_val:
                    return False
                if level % 2 == 1 and val >= prev_val:
                    return False
                
                prev_val = val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return True
