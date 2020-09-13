/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return recursive(l1, l2, 0);
        
    }
    
    ListNode* recursive(ListNode* l1, ListNode* l2, unsigned int overflow) 
    {
        ListNode* output = new ListNode();
        unsigned int value = overflow;
        if(l1) 
        {
            value += l1->val;
        }
        if(l2)
        {
            value += l2->val;
        }
        output->val = value%10;
        if((l1 && l1->next) || (l2 && l2->next) || (value>=10)) 
        {
            ListNode* l1next = 0;
            ListNode* l2next = 0;
            if(l1) {
                l1next = l1->next;
            }
            if(l2) {
                l2next = l2->next;
            }
            output->next = recursive(l1next, l2next, (value>=10)? 1 : 0);
        }
        else {
            output->next = 0;
        }
        return output;
        
    }
};