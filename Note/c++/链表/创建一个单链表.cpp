#include <iostream>
using namespace std;
/* 创建一个单链表 */
struct ListNode{
    int m_key;
    ListNode* next;
    ListNode(int x) : m_key(x), next(NULL) {}
};
ListNode* createList(ListNode* pHead) {
    ListNode* p = pHead;
    for (int i = 1; i < 10; ++i) {
        ListNode* pNewNode = new ListNode(i);
        p->next = pNewNode; // 上一个节点指向这个新建立的节点
        p = pNewNode; // p节点指向这个新的节点
    }
    return pHead;
}
int main(){
    ListNode* head = new ListNode(0);
    ListNode* tmp = createList(head);
    while(tmp != NULL) {
        cout << tmp->m_key << endl;
        tmp = tmp->next;
    }
    return 0;
}
