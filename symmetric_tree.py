"""
BFS: at each level, it should be a palindrome. TO show that, if a node has no child, then add them as NULL.
The whole node is added to the list to be checked as palindrome.
"""

from collections import deque
from typing import Optional



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfs(self, root):
        q = deque()
        q.append(root)

        while q:
            lst = []
            size = len(q)

            for _ in range(size):
                curr = q.popleft()
                lst.append(curr)

                if curr:
                    q.append(curr.left)
                    q.append(curr.right)

            # check palindrome
            i, j = 0, len(lst) - 1
            while i <= j:
                temp1 = lst[i]
                temp2 = lst[j]

                if not temp1 and not temp2:
                    i += 1
                    j -= 1
                    continue
                elif (not temp1 and temp2) or (temp1 and not temp2):
                    return False
                elif temp1.val != temp2.val:
                    return False

                i += 1
                j -= 1

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans = self.bfs(root)
        return ans
