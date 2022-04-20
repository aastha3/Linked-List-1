# brute force method O(n): tc 
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None: return head 
        slow = head
        
        if head.next==None and n==1:
            return None 
        
        if head.next.next==None and n ==2:
            return head.next
        else:
            head.next =None
            return head 
            
        fast = head.next 
        count = 2
        
        while fast!=None or fast.next!=None:
            slow = slow.next 
            fast = fast.next.next 
            count +=2
            
        if fast==None: count+=1 
        else: count+=1 
        
        ind = count-n 
        
        if count==n:
            return head.next 
        
        mid = int((count-n)/2)
        if ind > mid:
            cur = slow 
            travel = count -mid
        else:
            cur=head 
            travel = count -n 
            
        while travel>0:
            cur = cur.next 
            travel -=1
            
        cur = cur.next.next 
        
        return head