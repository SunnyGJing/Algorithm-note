"""
arg: ListNode* l1, ListNode* l2: 2个链表；
return: ListNode*: 2个非空链表分别按位存储了一个整数，用同样的存储格式，返回他们的和；
"""

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
    
    
class Solution_1 {
    // 简单地新建结点并插入到单链表中
    // O(n)+O(n)
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // 计算加和数值、进位数值
        int adds = (l1->val + l2->val) % 10;
        int remain = (l1->val + l2->val) / 10;
        // 头结点
        ListNode* head = new ListNode(adds);
        ListNode* p = head;
        // 为下一位做准备
        l1=l1->next;
        l2=l2->next;
        while(l1 && l2) {
            adds = (l1->val + l2->val + remain) % 10;
            remain = (l1->val + l2->val + remain) / 10;
            ListNode* pNode = new ListNode(adds);
            p->next = pNode;
            p = p->next;
            l1 = l1->next;
            l2 = l2->next;
        };
        while(l1) {
            adds = (l1->val + remain) % 10;
            remain = (l1->val + remain) / 10;
            ListNode* pNode = new ListNode(adds);
            p->next = pNode;
            p = p->next;
            l1 = l1->next;
        };
        while(l2) {
            adds = (l2->val + remain) % 10;
            remain = (l2->val + remain) / 10;
            ListNode* pNode = new ListNode(adds);
            p->next = pNode;
            p = p->next;
            l2 = l2->next;
        };
        if(remain != 0) {
            ListNode* pNode = new ListNode(remain);
            p->next = pNode;
        };
        return head;
    }
};


class toLearn_2 {
    // 用递归实现重复的插入和值节点的操作
    // O(n)+O(n)
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == NULL and l2 == NULL) return NULL;
        else if (l1 == NULL) return l2;
        else if (l2 == NULL) return l1;

        int adds = l1->val + l2->val;
        ListNode* head = new ListNode(adds % 10);
        head->next = addTwoNumbers(l1->next, l2->next);
        if(adds>9) {
            head->next = addTwoNumbers(head->next, new ListNode(1));
        };
        return head;
    }
};
