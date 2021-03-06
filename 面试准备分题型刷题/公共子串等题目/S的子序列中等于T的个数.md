
```
题目：  
leetcode 115
```

### 题解
#### 1. 动态规划状态转移式：(解法 1 特别慢)
```
    dp[i][0] = 1                                                    for all i
    dp[0][j] = 0                                                    for all j != 0
    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]                      if S[i] == T[j]
    dp[i][j] = dp[i - 1][j]                                         if S[i] != T[j]
```
Note：
1. 对dp状态转移方程的解释
    - 如果 S[i-1] 与 T[j-1] 相等，说明当前匹配的子序列个数由两项相加：
        - dp[i - 1][j]：前面的部分S[0..i-2]的子序列与T[0....j-1]匹配的个数（可以理解为其它字母已完成的成就，巨人的肩膀）
        - dp[i - 1][j - 1]：S[0..i-2]与T[0..j-2]匹配的个数（可以理解为字母S[i-1]所做的成就）
    - 如果 S[i-1] 与 T[j-1] 不相等，当前匹配的子序列个数等于：
        - dp[i - 1][j]：前面的部分S[0..i-2]的子序列与T[0....j-1]匹配的个数（可以理解为其它字母已完成的成就，巨人的肩膀）
2. dp数组初始化
    - 为了省去初始化base case的步骤，我们让dp的大小为(n + 1) * (m + 1)。
    - dp[i][0]表示在长度为i的S中找出与长度为0的T相等的子序列的个数，因为空串是任意字符串的子串，所以可知dp[i][0] = i
    - dp[0][j]表示在长度为0的S中找出与长度为i的T相等的子序列的个数，要按i的值分情况讨论：
        - 如果j=0，表示S为空串，T为空串，因为空串是空串的子串，所以可知dp[0][0]=1
        - 如果j!=0，表示S为空串，T不是空串，因为空串没有除了空串之外的子串，所以可知dp[0][j]=1

### Code
##### 解法
```python
def numDistinct(s, t):
    m, n = len(s), len(t)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m):
        dp[i][0] = 1    # 空串是任何字符串的子串，此外，空串是空串的子串
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]
```