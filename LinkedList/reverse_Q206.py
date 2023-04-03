# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head==None:
        #     return None
        # itr=head
        # new_head=None
        # prev_node=itr
        # curr_node=itr.next
        # next_node=curr_node.next
        # while curr_node.next!=None:
        #     curr_node=next_node
        #     next_node=curr_node.next
        #     curr_node.next=prev_node
        #     prev_node=curr_node

        itr=head
        tmp=[]
        while itr!=None:
            tmp.append(itr.val)
            # print(tmp[0])
            itr=itr.next
        
        cnt=len(tmp)-2
        tmp=reversed(tmp)
        flag=0
        new_head=None
        itr=None
        for i in tmp:
            if flag==0:
                new_node=ListNode(i)
                itr=new_node
                new_head=new_node
                flag=1
            else:
                new_node=ListNode(i)
                itr.next=new_node
                itr=new_node
        return new_head


        # new_head=ListNode(tmp[len(tmp)-1],None)
        # itr=new_head
        # while cnt!=-1:
        #     tmp_node=ListNode(tmp[cnt],None)
        #     itr.next=tmp_node
        #     itr=tmp_node
        #     cnt-=1
        # return new_head






            
        
        