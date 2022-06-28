class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return 
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        res=head=ListNode()
        
        while list1 and list2:
            print(list1.val,list2.val)
            if list1.val <= list2.val:
                head.next=list1
                list1=list1.next
                head=head.next
            else:
                head.next=list2
                head=head.next
                list2=list2.next  
                
        while list1:
            head.next=list1
            head=head.next
            list1=list1.next
        while list2:
            head.next=list2
            head=head.next
            list2=list2.next 
            
            
        return res.next
