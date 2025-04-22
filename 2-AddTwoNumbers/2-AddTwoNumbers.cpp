// Last updated: 22/04/2025 16:50:38
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
        ListNode* dummyNode = new ListNode(0);
        ListNode* final = dummyNode;
        int res;
        int retenue = 0;
        while(l1 != nullptr || l2 != nullptr || retenue != 0){
            res = retenue;
            retenue = 0;
            if(l1 != nullptr){
                res = res + l1->val;
                l1 = l1->next;
            }
            if(l2 != nullptr){
                res = res + l2->val;
                l2 = l2->next;
            }
            if(res >= 10){
                retenue = res/10;
                res = res % 10;
            }
            final->next = new ListNode(res);
            final = final->next;
        }
        return dummyNode->next;
    }
};