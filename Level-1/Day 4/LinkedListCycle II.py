# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
      # Using Floyd's Tortoise and Hare technique
      
        slow,fast=head,head
        if not head: return
        
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if fast == slow:
                break
        slow2=head
        if not fast.next or not fast.next.next: return
        
        while slow.next:
            if slow==slow2: return slow2
            slow2=slow2.next
            slow=slow.next
        return 
