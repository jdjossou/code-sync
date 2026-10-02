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
    ListNode* mergeKLists(vector<ListNode*>& lists) {

        priority_queue<ListNode*, vector<ListNode*>, decltype([](const ListNode* a, const ListNode* b) -> bool {
            return a->val > b->val;
        })> pq;

        for (ListNode* list : lists) {
            if (list != nullptr) pq.push(list);
        }

        auto merge = [&pq](this auto self) -> ListNode* {
            if (pq.empty()) {
                return nullptr;
            }

            ListNode* min = pq.top();
            pq.pop();

            if (min->next != nullptr) {
                pq.push(min->next);
            }

            return new ListNode(min->val, self());
        };

        return merge();
    }
};