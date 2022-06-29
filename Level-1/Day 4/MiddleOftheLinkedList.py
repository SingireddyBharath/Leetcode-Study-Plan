# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        length=0
        temp=head
        while head:     
            head=head.next
            length+=1
            
        length=length//2+1
        i=1
        while i<length:     
            temp=temp.next
            i+=1         
                 
        return temp
