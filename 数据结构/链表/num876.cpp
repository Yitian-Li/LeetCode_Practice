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
    ListNode* middleNode(ListNode* head) {
        ListNode* p = head;
        int count = 0;
        while(p){
            count++;
            p = p->next;
        }
        int mid = count/2+1;
        p = head;
        for(int i=1; i < mid; i++){
            p = p->next;
        }
        return p;
    }
};