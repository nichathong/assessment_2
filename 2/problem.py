from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#We will need to use BFS because we require to look into each level -> using queue
    # want to look closely at the nodes on the same level as 'u'
    # if we reach til the end and coudn't find other node that is on the same level as 'u' then return null
    #check if current == node u?
        # if it is then the next node on the same level is the answer > compare if level_num is equal
        #else:progress to to the next level
#edge case
    # empty  -> return null



#
class Solution:
    def findNearestRightNode(self, root, u):
        if not root:
            return None
        
        queue = deque([(root, 0)])
        while queue:
            current, level_num = queue.popleft()

            if current == u:
                if queue and queue[0][1] == level_num:
                    return queue[0][0]
                else:
                    return None
            
            if current.left is not None:
                queue.append((current.left, level_num + 1))
            if current.right is not None:
                queue.append((current.right, level_num + 1))
        
        return None