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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL){
            return NULL;
        }
        // 将链表尾部指向链表头部，形成循环
        int length = 1;
        ListNode* p = head;
        while(p->next != NULL){
            p = p->next;
            length++;
        }
        p->next = head;
        int move = length - k % length; 
        // move
        ListNode *newtail = head;
        for (int i=0; i<move-1; i++){
            newtail = newtail->next;
        }
        // 断开循环
        ListNode *newhead = newtail->next;
        newtail->next = NULL;
        return newhead;
    }
};