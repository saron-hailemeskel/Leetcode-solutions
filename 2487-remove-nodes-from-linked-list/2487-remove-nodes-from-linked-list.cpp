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
private:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

public:
    ListNode* removeNodes(ListNode* head) {
        if (!head || !head->next) return head;

        // 1. Reverse the list so we can traverse from right to left
        head = reverseList(head);
        
        ListNode* curr = head;
        int maxVal = curr->val;
        
        // 2. Keep nodes that are >= the max value seen so far
        while (curr != nullptr && curr->next != nullptr) {
            if (curr->next->val < maxVal) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
                maxVal = curr->val;
            }
        }
        
        // 3. Reverse back to restore the original order
        return reverseList(head);
    }
};