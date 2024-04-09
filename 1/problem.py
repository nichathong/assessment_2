class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# question ask to remove duplicate
# since it is sorted -> the number will appear in order
# we can start by traverse through linked link
    #check if current.val == current.next.val?
    #if it's equal then we want to remove
        #to remove
            # current.next= current.next.next
            #
            #else current = current.next
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        current = head

        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
        
        