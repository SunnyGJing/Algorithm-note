```
递归：
    前序、中序、后序基本相同
非递归：
    前序、中序基本相同；后序难一点

陈先生让我看的文章链接：
https://blog.csdn.net/qq_33278461/article/details/89036595
```

#### Code
##### 解法
```python
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preOrderRecurion(pHead):
    if not pHead: return

    print(pHead.value)
    preOrderRecurion(pHead.left)
    preOrderRecurion(pHead.right)


def preOrderNoRecurion(pHead):
    stack = []
    cur = pHead
    while cur or stack:
        while cur:
            print(cur.value)
            stack.append(cur)
            cur = cur.left
        if stack:
            cur = stack[-1]
            stack.pop()
            cur = cur.right


def inOrderRecurion(pHead):
    if not pHead: return

    inOrderRecurion(pHead.left)
    print(pHead.value)
    inOrderRecurion(pHead.right)


def inOrderNoRecurion(pHead):
    stack = []
    cur = pHead
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        if stack:
            cur = stack[-1]
            print(cur)
            stack.pop()
            cur = cur.right


def postOrderRecurion(pHead):
    if not pHead: return

    postOrderRecurion(pHead.left)
    postOrderRecurion(pHead.right)
    print(pHead.value)


def postOrderNoRecurion_1(root):
    stack = [root]  # 根节点提前入栈
    cur, pre = None, None

    while stack:
        cur = stack[-1]
        if (cur.left is None and cur.right is None) or (pre and (pre == cur.right or pre == cur.left)):
            # 如果当前结点没有孩子节点或者孩子节点都已被访问过
            print(cur.value)
            stack.pop()
            pre = cur
        else:
            # 右孩子先入栈、左孩子后入栈
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)


def postOrderNoRecurion_2(root):
    if not root: return

    stack1, stack2 = [], []
    stack1.append(root)

    while stack1:
        cur = stack1[-1]
        stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack2.append(cur.left)
        if cur.right:
            stack2.append(cur.right)
    while stack2:   # stack2保存的就是后序遍历的序列(只不过是反向顺序保存)，挨个出栈即可
        print(stack2[-1])
        stack2.pop()



def generateTree():
    pHead = Node(0)
    pNode = pHead
    pNode.left = Node(1)
    pNode.right = Node(2)
    pNode = pNode.left
    pNode.left = Node(3)
    pNode.right = Node(4)
    pNode = pNode.right
    pNode.left = Node(10)
    pNode.right = Node(11)
    pNode = pHead.right
    pNode.left = Node(5)
    pNode.right = Node(6)

    return pHead



if __name__ == "__main__":
    pHead = generateTree()

    preOrderRecurion(pHead)
    preOrderNoRecurion(pHead)
    inOrderRecurion(pHead)
    inOrderNoRecurion(pHead)
    postOrderRecurion(pHead)
    postOrderNoRecurion_1(pHead)
    postOrderNoRecurion_2(pHead)
```