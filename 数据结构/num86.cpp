/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *before=new ListNode(0);
        ListNode *after=new ListNode(0);
        ListNode *p1=before,*p2=after;
        if(!head)
        return head;
        while(head)
        {
            if(head->val<x)
            {
                p1->next=head;
                p1=p1->next;
                head=head->next;
            }
            else
            {
                p2->next=head;
                p2=p2->next;
                head=head->next;
            }
        }
        //将before和after连起来
        p2->next=NULL;
        p1->next=after->next;
        return before->next;
    }
};