class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # length of first LL
        i = 0
        firstList = l1
        while l1.next != None:
            i += 1
            l1 = l1.next
        length1 = i+1
        
        # length of second LL
        j = 0
        secondList = l2
        while l2.next != None:
            j +=1
            l2 = l2.next
        length2 = j + 1
            
        # set l1 and l2 to first Node  
        l1 = firstList
        l2 = secondList
        
        elems = []
        if length1 == length2:
            rem = 0
            while l1.next != None:
                a = l1.val + l2.val + rem
                sum = a % 10
                elems.append(ListNode(sum, None))
                rem = a // 10
                
                l1 = l1.next
                l2 = l2.next
            
            a = l1.val + l2.val + rem
            sum = a % 10
            elems.append(ListNode(sum, None))
            rem = a // 10
            if rem != 0:
                elems.append(ListNode(rem, None))
                
        elif length1 < length2:
            rem = 0
            while l2.next != None:
                if l1 == None:
                    l1 = ListNode(0, None)
                    l1.val = 0
                    l1.next = None
                    
                a = l1.val + l2.val + rem
                sum = a % 10
                elems.append(ListNode(sum, None))
                rem = a // 10
                
                l1 = l1.next
                l2 = l2.next
                
            
            a = l2.val + rem
            sum = a % 10
            elems.append(ListNode(sum, None))
            rem = a // 10
            if rem != 0:
                elems.append(ListNode(rem, None))
                
        elif length1 >length2:
            rem = 0
            while l1.next != None:
                if l2 == None:
                    l2 = ListNode(0, None)
                    l2.val = 0
                    l2.next = None
                    
                a = l1.val + l2.val + rem
                sum = a % 10
                elems.append(ListNode(sum, None))
                rem = a // 10
                
                l1 = l1.next
                l2 = l2.next
                
            
            a = l1.val + rem
            sum = a % 10
            elems.append(ListNode(sum, None))
            rem = a // 10
            if rem != 0:
                elems.append(ListNode(rem, None))
                
            
        # add next to each Node of solution  
        for l in elems:
            if l != elems[-1]:
                l.next = elems[elems.index(l)+1]
            else:
                l.next = None
                
        # return first Node        
        return elems[0]
