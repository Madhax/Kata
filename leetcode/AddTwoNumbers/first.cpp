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
        unsigned long long int result =  recursive(1, l1) + recursive(1, l2);
        if(result == 0) {
            ListNode *value = new ListNode();
            value->val = 0;
            return value;
        }
        return buildListNode(result);
    }
    
    unsigned long long int recursive(unsigned long long int level, ListNode* l1) {
        if(!(l1))
            return 0;
        return level * l1->val + recursive(level*10, l1->next);
    }
    
    ListNode* buildListNode(unsigned long long int number) {
        if(number == 0) {
            return 0;
        }
        ListNode* entry = new ListNode();
        entry->val = number%10;
        entry->next = buildListNode((number-(entry->val))/10);
        return entry;
    }
};