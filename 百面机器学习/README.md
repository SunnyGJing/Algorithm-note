# Week 1
## 机器学习
分类算法

- 逻辑回归
    - 极大似然估计(详见P59)
        - 似然：通过样本猜测总体
    - 梯度下降法推导（详见[博客](https://blog.csdn.net/pengchengliu/article/details/80932232)）
    - 逻辑回归推导（详见[博客](https://zhuanlan.zhihu.com/p/44591359)）
        - 在线性回归外层套一个sigmoid（将$(-\infty,\infty)$映射到$(0,1)$之间）
- 决策树
    - ID3 信息增益 仅离散属性
    - C4.5 信息增益比 = 信息增益/划分前熵 连续值
    - CART Gini指数（集合的不确定性） 仅二叉树
    - 剪枝（防止过拟合）
        - 预剪枝
        - 后剪枝（剪掉叶结点较少的分支）
- softmax交叉熵
    - 推导过程（详见[博客]()）

## 算法
- 快速排序
    - 挖坑法（双指针）
    - 指针交换法（交换数据）
- 堆排序
- 双指针
    - 对撞指针
    - 快慢指针
    - 滑动窗口


### 题目
#### 算法刷题重点题型

- [x] 双指针（167）：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted

- [x] 快速选择、堆排序、归并排序（215）：https://leetcode-cn.com/problems/kth-largest-element-in-an-array

- [x] 桶排序（347）：https://leetcode-cn.com/problems/top-k-frequent-elements

- [x] 滑动窗口（209）：https://leetcode-cn.com/problems/minimum-size-subarray-sum/

    - 长度最小的连续子数组
  
- [x] 滑动窗口（438）：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

    - 找到字符串中所有字母异位词

- [x] 滑动窗口（76）：https://leetcode-cn.com/problems/minimum-window-substring/
    
    - 最小覆盖子串

#### 算法刷题课后作业
- [x] 数组中重复的数字：https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8

- [x] 构建乘积数组：https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46

- [x] 二维数组中的查找：https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e

# Week 2
## 机器学习
- SVM
    - 线性可分
    - 超平面 最大间隔超平面（最近的样本点到平面的距离）
    - 支持向量（距离超平面最近的点）
    - SVM的最优化问题
    - 对偶问题
        - 构造拉格朗日函数
        - min(max(f))=max(min(f))（强对偶关系）
        - KKT约束条件（强对偶性的充要条件）
        - SMO（序列最小优化）算法求λ∗
    - 软间隔（允许个别样本点出现在间隔带里）
        - 松弛变量ξ
    - 核函数（线性不可分）
        - 非线性SVM（映射到更高维度）
        - k(xi,xj)=ϕ(xi)ϕ(xj)减少映射的计算量
        - 常用核函数
            - 线性核函数
            - 多项式核（不平稳，数据已归一化）
            - RBF核（高斯核）γ（最常用）
- 降维 PCA和LDA
    - PCA
        - 最大化投影的方差
    - LDA（Linear Discriminant Analysis）有监督
        - 最大化类间距离以及最小化类内距离
## 算法
- KMP算法
    - 字符串匹配
    - 空间换时间
    - 部分匹配表PMT：记录字符串前缀集合和后缀集合交集中最长元素长度（子字符串p）
        - 向右移动一位得到next数组，0位填-1
        - 根据p求解next
- 二分搜索
    - while left <= right if right = str.len - 1
    - mid = lower + (upper - lower) // 2 防止溢出
    - 目标有多个重复
        - 最左侧
            - left = 0 right = str.len # [)
            - while left < right # [left, left)
            - mid = (left + right) // 2
            - if str[mid] == target: right = mid
            - if str[mid] < target: left = mid + 1
            - if str[mid] > target: right = mid
            - return left
        - 最右侧
            - left = 0 right = str.len # [)
            - while left < right # [right, right)
            - mid = (left + right) // 2
            - if str[mid] == target: left = mid + 1
            - if str[mid] < target: left = mid + 1
            - if str[mid] > target: right = mid
            - return left - 1
- 哈希表
### 题目
#### 算法刷题重点题型
- [x] 替换空格：https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423

- [x] 正则表达式匹配：https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c

- [x] 表示数值的字符串：https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2

- [x] 字符流中第一个不重复的字符：https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720

- [ ] 二分搜索（69）：https://leetcode-cn.com/problems/sqrtx/

- [x] 哈希表（1）：https://leetcode-cn.com/problems/two-sum/

- [x] 旋转数组的最小数字：https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba

#### 算法刷题课后作业
- [x] 左旋转字符串：https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec

- [x] 字符串的排列：https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ﬀdd9a96c7

- [x] 第一个只出现一次的字符：https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c

- [ ] 在排序数组中查找元素的第一个和最后一个位置（34）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

- [ ] 找到 K 个最接近的元素（658）：https://leetcode-cn.com/problems/find-k-closest-elements/

- [ ] 长度最小的子数组（209）：https://leetcode-cn.com/problems/minimum-size-subarray-sum/

- [ ] 有序矩阵中第 K 小的元素（378）：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Week 3
## 机器学习
- K-means
    - EM（Expectation Maximum）算法
    - 收敛性证明
## 算法
- 虚拟头结点
- 删除链表中重复的结点
  - 3指针：基准、快、慢
- 链表中环的入口结点
  - 哈希表
  - 快慢指针
- 栈和队列
  - 由链表实现 [].pop(0) [].pop()
### 题目
#### 算法刷题重点题型
- [ ] 删除链表中重复的结点：https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef

- [ ] 链表中环的入口结点：https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4

- [ ] 用两个栈实现队列：https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6

- [ ] 滑动窗口的最大值：https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788

#### 算法刷题课后作业
- [ ] 从尾到头打印链表：https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035

- [ ] 相交链表（160）：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

- [ ] 用栈实现队列（232）：https://leetcode-cn.com/problems/implement-queue-using-stacks/

# Week 4
## 机器学习
- HMM
    - 概率模型
        - 生成模型 联合概率分布
        - 判别模型 条件概率分布
    - 基本假设
        - 齐次马尔可夫假设
        - 观测独立性检测
    - 基本问题
        - 概率计算：计算观测值的概率
          - 直接计算
          - 前向、后向算法（DP）
        - 预测/解码：通过观测序列求状态序列
          - 维特比算法（DP）
        - 学习/训练：计算λ
          - 有监督
          - 无监督：仅观测序列
            - Baum-Welch算法
        - 实例
          - from hmmlearn import hmm
- CRF
## 算法
- DFS和BFS
    - BFS (279)
      - 队列
      - 邻接表 O(V)+O(E)
      - 临界矩阵 O(V2)
    - DFS (695)
      - 递归
      - 栈-非递归
      - 树的前序遍历
- 最短路径
    - Dijkstra (743)
      - 1点到其它，每次确定一个结点
      - 记录上一个结点可得到路径
      - 权值非负
      - O(V2+E) 稀疏图
    - Bellman-Ford
      - 权值可以为负（负环）
      - 循环遍历所有边，直到所有值不改变（最多N-1）
      - O(VE)
- 最小生成树 图的最小连通子图
    - 并查集 用集合中的一个元素代表集合（帮会）(684)
    - Kruskal (1135)
      - 对边排序，从小到大并查集
    - Prim
      - 从某顶点开始，每次吸纳1个结点
- 二叉树的遍历（stack非递归较复杂）
    - 前序
    - 中序
    - 后序
    - 层次（queue）
- 二叉搜索树和平衡二叉树
    - |左右子树高度之差|<=1
    - 搜索
    - 插入
      - 平衡（只调整失衡的第一个结点）
        - 左-左
          - 右旋
        - 右-右
        - 左-右
          - 左旋（产生左-左）->右旋
        - 右-左
    - 删除
      - 结点不存在
      - 叶子节点
      - 有1个孩子
      - 有2个孩子
      - 平衡
### 题目
#### 算法刷题重点题型
树类问题：

- [ ] 平衡二叉树（110）：https://leetcode-cn.com/problems/balanced-binary-tree

- [ ] 找树左下角的值（513）：https://leetcode-cn.com/problems/find-bottom-left-tree-value

- [ ] 二叉树展开为链表（114）：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

- [ ] 二叉搜索树中第K小的元素（230）：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/ description/

- [ ] 实现 Trie (前缀树)（208）：https://leetcode-cn.com/problems/implement-trie-prefix-tree

- [ ] 序列化二叉树：https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84

- [ ] 重建二叉树：https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6

图类问题：

- [ ] 判断二分图（785）：https://leetcode-cn.com/problems/is-graph-bipartite

- [ ] 拓扑排序（207）：https://leetcode-cn.com/problems/course-schedule

- [ ] 并查集（684）：https://leetcode-cn.com/problems/redundant-connection

- [ ] 岛屿的最大面积（695）：https://leetcode-cn.com/problems/max-area-of-island/

    - DFS或BFS
#### 算法刷题课后作业
- [ ] 对称的二叉树：https://www.nowcoder.com/practice/ﬀ05d44dfdb04e1d83bdbdab320efbcb

- [ ] 把二叉树打印成多行：https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288

- [ ] 二叉树的下一个结点：https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e

- [ ] 数据流中的中位数：https://www.nowcoder.com/practice/9be0172896bd43948f8a32fb954e1be1

- [ ] 二叉搜索树的第k个结点：https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a

- [ ] 按之字形顺序打印二叉树：https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0

- [ ] 完全平方数（279）：https://leetcode-cn.com/problems/perfect-squares/

    - 从n到0每个数字表示1个结点，相差1个完全平方数的结点有边，找0到n的最短路径
- [ ] 电话号码的字母组合（17）：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

# Week 5
## 机器学习
- 前向神经网络
- 序列数据中常用的循环神经网络
  - RNN
  - GRU和LSTM
## 算法
- 递归
  - 记忆化搜索
  - 跳台阶 (509)
  - 变态跳台阶 (牛客)
- 回溯法（反向递归树）
  - 递归一定会发生回溯 暴力搜索
  - 全排列 (46) 恢复标志位
  - 机器人运动范围 (面试题13)
- 动态规划DP
  - 保存子问题的答案
  - 自下而上（与记忆化搜索相反）
  - 0/1背包问题 (416. 分割等和子集)
    - 挑选的物品只有一个
    - 该物品可选可不选
      - 状态
    - dp[i][j] 挑选第i个物品放入j容量的最大价值
      - 状态转移方程
      - 空间：$O(nC)−>O(2C)（只保留上一行）−>O(C)$（倒序更新）
      - 时间：$O(nC)$ 物品数量背包容量
  - 最长上升子序列LIS (300)
    - dp[i] 以第i个数字结尾的LIS长度
    - dp[i] = max([dp[j] + 1 for j in range(i) if nums[i] > nums[j]] + [1])
  - 最长公共子序列LCS (1143)
    - dp[i][j] s1的前i个字符和s2的前j的字符的LCS的大小
    - dp[i][j] = dp[i-1][j-1]+1 s1[i] == s2[j]
    - dp[i][j] = max(dp[i-1][j], dp[i][j-1]) s1[i] != s2[j]
### 题目
#### 算法刷题重点题型
递归、回溯问题：

- [ ] 斐波那契数列：https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3

- [ ] 跳台阶：https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4

- [ ] 变态跳台阶：https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387

- [ ] 全排列（46）：https://leetcode-cn.com/problems/permutations/

- [ ] 机器人的运动范围：https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8

动态规划问题：

- [ ] 斐波那契数列（用DP方法再写一下）（70）：https://leetcode-cn.com/problems/climbing-stairs

- [ ] 0-1 背包（416）：https://leetcode-cn.com/problems/partition-equal-subset-sum

- [ ] 最长递增子序列（300）：https://leetcode-cn.com/problems/longest-increasing-subsequence

- [ ] 最长公共子序列（1143）：https://leetcode-cn.com/problems/longest-common-subsequence/

#### 算法刷题课后作业
- [ ] 矩阵中的路径：https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc

- [ ] 矩形覆盖：https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6

- [ ] 矩阵路径（64）：https://leetcode-cn.com/problems/minimum-path-sum

- [ ] 股票交易（309）：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

- [ ] 字符串编辑（583）：https://leetcode-cn.com/problems/delete-operation-for-two-strings

- [ ] 数组区间（303）：https://leetcode-cn.com/problems/range-sum-query-immutable

- [ ] 分割整数（343）：https://leetcode-cn.com/problems/integer-break

# Week 6
## 机器学习
- 集成学习
- XGBoost
## 算法
- 贪心算法






---------


# 值得做的LeetCode题
```
https://github.com/Relph1119/QuestForMachineLearning-Camp/blob/master/PhaseThree/LeetCode/README.md
```

## 双指针

[167. Two Sum II - Input array is sorted (Easy)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

[633. Sum of Square Numbers (Easy)](https://leetcode.com/problems/sum-of-square-numbers/description/)

[345. Reverse Vowels of a String (Easy)](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)

[680. Valid Palindrome II (Easy)](https://leetcode.com/problems/valid-palindrome-ii/description/)

[88. Merge Sorted Array (Easy)](https://leetcode.com/problems/merge-sorted-array/description/)

[141. Linked List Cycle (Easy)](https://leetcode.com/problems/linked-list-cycle/description/)

[524. Longest Word in Dictionary through Deleting (Medium)](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/)

## 排序

[215. Kth Largest Element in an Array (Medium)](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

[347. Top K Frequent Elements (Medium)](https://leetcode.com/problems/top-k-frequent-elements/description/)

[451. Sort Characters By Frequency (Medium)](https://leetcode.com/problems/sort-characters-by-frequency/description/)

[75. Sort Colors (Medium)](https://leetcode.com/problems/sort-colors/description/)

## 贪心思想

[455. Assign Cookies (Easy)](https://leetcode.com/problems/assign-cookies/description/)

[435. Non-overlapping Intervals (Medium)](https://leetcode.com/problems/non-overlapping-intervals/description/)

[452. Minimum Number of Arrows to Burst Balloons (Medium)](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/)

[406. Queue Reconstruction by Height(Medium)](https://leetcode.com/problems/queue-reconstruction-by-height/description/)

[763. Partition Labels (Medium)](https://leetcode.com/problems/partition-labels/description/)

[605. Can Place Flowers (Easy)](https://leetcode.com/problems/can-place-flowers/description/)

[392. Is Subsequence (Medium)](https://leetcode.com/problems/is-subsequence/description/)

[665. Non-decreasing Array (Easy)](https://leetcode.com/problems/non-decreasing-array/description/)

[122. Best Time to Buy and Sell Stock II (Easy)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

[53. Maximum Subarray (Easy)](https://leetcode.com/problems/maximum-subarray/description/)

[121. Best Time to Buy and Sell Stock (Easy)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## 二分查找

[69. Sqrt(x) (Easy)](https://leetcode.com/problems/sqrtx/description/)

[744. Find Smallest Letter Greater Than Target (Easy)](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/)

[540. Single Element in a Sorted Array (Medium)](https://leetcode.com/problems/single-element-in-a-sorted-array/description/)

[278. First Bad Version (Easy)](https://leetcode.com/problems/first-bad-version/description/)

[153. Find Minimum in Rotated Sorted Array (Medium)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

[34. Search for a Range (Medium)](https://leetcode.com/problems/search-for-a-range/description/)

## 分治

[241. Different Ways to Add Parentheses (Medium)](https://leetcode.com/problems/different-ways-to-add-parentheses/description/)

## 搜索

### BFS

[279. Perfect Squares (Medium)](https://leetcode.com/problems/perfect-squares/description/)

[127. Word Ladder (Medium)](https://leetcode.com/problems/word-ladder/description/)

### DFS

[695. Max Area of Island (Easy)](https://leetcode.com/problems/max-area-of-island/description/)

[200. Number of Islands (Medium)](https://leetcode.com/problems/number-of-islands/description/)

[547. Friend Circles (Medium)](https://leetcode.com/problems/friend-circles/description/)

[130. Surrounded Regions (Medium)](https://leetcode.com/problems/surrounded-regions/description/)

[417. Pacific Atlantic Water Flow (Medium)](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

### Backtracking

[17. Letter Combinations of a Phone Number (Medium)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

[93. Restore IP Addresses(Medium)](https://leetcode.com/problems/restore-ip-addresses/description/)

[79. Word Search (Medium)](https://leetcode.com/problems/word-search/description/)

[257. Binary Tree Paths (Easy)](https://leetcode.com/problems/binary-tree-paths/description/)

[46. Permutations (Medium)](https://leetcode.com/problems/permutations/description/)

[47. Permutations II (Medium)](https://leetcode.com/problems/permutations-ii/description/)

[77. Combinations (Medium)](https://leetcode.com/problems/combinations/description/)

[39. Combination Sum (Medium)](https://leetcode.com/problems/combination-sum/description/)

[40. Combination Sum II (Medium)](https://leetcode.com/problems/combination-sum-ii/description/)

[216. Combination Sum III (Medium)](https://leetcode.com/problems/combination-sum-iii/description/)

[78. Subsets (Medium)](https://leetcode.com/problems/subsets/description/)

[90. Subsets II (Medium)](https://leetcode.com/problems/subsets-ii/description/)

[131. Palindrome Partitioning (Medium)](https://leetcode.com/problems/palindrome-partitioning/description/)

[37. Sudoku Solver (Hard)](https://leetcode.com/problems/sudoku-solver/description/)

[51. N-Queens (Hard)](https://leetcode.com/problems/n-queens/description/)

## 动态规划

### 斐波那契数列

[70. Climbing Stairs (Easy)](https://leetcode.com/problems/climbing-stairs/description/)

[198. House Robber (Easy)](https://leetcode.com/problems/house-robber/description/)

[213. House Robber II (Medium)](https://leetcode.com/problems/house-robber-ii/description/)


### 矩阵路径

[64. Minimum Path Sum (Medium)](https://leetcode.com/problems/minimum-path-sum/description/)

[62. Unique Paths (Medium)](https://leetcode.com/problems/unique-paths/description/)

### 数组区间

[303. Range Sum Query - Immutable (Easy)](https://leetcode.com/problems/range-sum-query-immutable/description/)

[413. Arithmetic Slices (Medium)](https://leetcode.com/problems/arithmetic-slices/description/)

### 分割整数

[343. Integer Break (Medim)](https://leetcode.com/problems/integer-break/description/)

[279. Perfect Squares(Medium)](https://leetcode.com/problems/perfect-squares/description/)

[91. Decode Ways (Medium)](https://leetcode.com/problems/decode-ways/description/)

### 最长递增子序列

[300. Longest Increasing Subsequence (Medium)](https://leetcode.com/problems/longest-increasing-subsequence/description/)

[646. Maximum Length of Pair Chain (Medium)](https://leetcode.com/problems/maximum-length-of-pair-chain/description/)

[376. Wiggle Subsequence (Medium)](https://leetcode.com/problems/wiggle-subsequence/description/)

### 最长公共子序列

### 0-1 背包

[416. Partition Equal Subset Sum (Medium)](https://leetcode.com/problems/partition-equal-subset-sum/description/)

[494. Target Sum (Medium)](https://leetcode.com/problems/target-sum/description/)

[139. Word Break (Medium)](https://leetcode.com/problems/word-break/description/)

[474. Ones and Zeroes (Medium)](https://leetcode.com/problems/ones-and-zeroes/description/)

[322. Coin Change (Medium)](https://leetcode.com/problems/coin-change/description/)

[377. Combination Sum IV (Medium)](https://leetcode.com/problems/combination-sum-iv/description/)

### 股票交易

[309. Best Time to Buy and Sell Stock with Cooldown(Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

[714. Best Time to Buy and Sell Stock with Transaction Fee (Medium)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/)

[123. Best Time to Buy and Sell Stock III (Hard)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/)

[188. Best Time to Buy and Sell Stock IV (Hard)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/)

### 字符串编辑

[583. Delete Operation for Two Strings (Medium)](https://leetcode.com/problems/delete-operation-for-two-strings/description/)

[72. Edit Distance (Hard)](https://leetcode.com/problems/edit-distance/description/)

[650. 2 Keys Keyboard (Medium)](https://leetcode.com/problems/2-keys-keyboard/description/)

## 数学

### 素数

[204. Count Primes (Easy)](https://leetcode.com/problems/count-primes/description/)

### 进制转换

[504. Base 7 (Easy)](https://leetcode.com/problems/base-7/description/)

[405. Convert a Number to Hexadecimal (Easy)](https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/)

[168. Excel Sheet Column Title (Easy)](https://leetcode.com/problems/excel-sheet-column-title/description/)

### 阶乘

[172. Factorial Trailing Zeroes (Easy)](https://leetcode.com/problems/factorial-trailing-zeroes/description/)

### 字符串加法减法

[67. Add Binary (Easy)](https://leetcode.com/problems/add-binary/description/)

[415. Add Strings (Easy)](https://leetcode.com/problems/add-strings/description/)

### 相遇问题

[462. Minimum Moves to Equal Array Elements II (Medium)](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)

### 多数投票问题

[169. Majority Element (Easy)](https://leetcode.com/problems/majority-element/description/)

### 其它

[367. Valid Perfect Square (Easy)](https://leetcode.com/problems/valid-perfect-square/description/)

[326. Power of Three (Easy)](https://leetcode.com/problems/power-of-three/description/)

[238. Product of Array Except Self (Medium)](https://leetcode.com/problems/product-of-array-except-self/description/)

[628. Maximum Product of Three Numbers (Easy)](https://leetcode.com/problems/maximum-product-of-three-numbers/description/)

# 数据结构相关

## 链表

[160. Intersection of Two Linked Lists (Easy)](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)

[206. Reverse Linked List (Easy)](https://leetcode.com/problems/reverse-linked-list/description/)

[21. Merge Two Sorted Lists (Easy)](https://leetcode.com/problems/merge-two-sorted-lists/description/)

[83. Remove Duplicates from Sorted List (Easy)](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

[19. Remove Nth Node From End of List (Medium)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

[24. Swap Nodes in Pairs (Medium)](https://leetcode.com/problems/swap-nodes-in-pairs/description/)

[445. Add Two Numbers II (Medium)](https://leetcode.com/problems/add-two-numbers-ii/description/)

[234. Palindrome Linked List (Easy)](https://leetcode.com/problems/palindrome-linked-list/description/)

[725. Split Linked List in Parts(Medium)](https://leetcode.com/problems/split-linked-list-in-parts/description/)

[328. Odd Even Linked List (Medium)](https://leetcode.com/problems/odd-even-linked-list/description/)

## 树

### 递归

[104. Maximum Depth of Binary Tree (Easy)](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)

[110. Balanced Binary Tree (Easy)](https://leetcode.com/problems/balanced-binary-tree/description/)

[543. Diameter of Binary Tree (Easy)](https://leetcode.com/problems/diameter-of-binary-tree/description/)

[226. Invert Binary Tree (Easy)](https://leetcode.com/problems/invert-binary-tree/description/)

[617. Merge Two Binary Trees (Easy)](https://leetcode.com/problems/merge-two-binary-trees/description/)

[Leetcdoe : 112. Path Sum (Easy)](https://leetcode.com/problems/path-sum/description/)

[437. Path Sum III (Easy)](https://leetcode.com/problems/path-sum-iii/description/)

[572. Subtree of Another Tree (Easy)](https://leetcode.com/problems/subtree-of-another-tree/description/)

[101. Symmetric Tree (Easy)](https://leetcode.com/problems/symmetric-tree/description/)

[111. Minimum Depth of Binary Tree (Easy)](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

[404. Sum of Left Leaves (Easy)](https://leetcode.com/problems/sum-of-left-leaves/description/)

[687. Longest Univalue Path (Easy)](https://leetcode.com/problems/longest-univalue-path/)

[337. House Robber III (Medium)](https://leetcode.com/problems/house-robber-iii/description/)

[671. Second Minimum Node In a Binary Tree (Easy)](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/)

### 层次遍历

[637. Average of Levels in Binary Tree (Easy)](https://leetcode.com/problems/average-of-levels-in-binary-tree/description/)

[513. Find Bottom Left Tree Value (Easy)](https://leetcode.com/problems/find-bottom-left-tree-value/description/)

### 前中后序遍历

[144. Binary Tree Preorder Traversal (Medium)](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

[145. Binary Tree Postorder Traversal (Medium)](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)

[94. Binary Tree Inorder Traversal (Medium)](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

### BST

[669. Trim a Binary Search Tree (Easy)](https://leetcode.com/problems/trim-a-binary-search-tree/description/)

[230. Kth Smallest Element in a BST (Medium)](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

[Convert BST to Greater Tree (Easy)](https://leetcode.com/problems/convert-bst-to-greater-tree/description/)

[235. Lowest Common Ancestor of a Binary Search Tree (Easy)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

[236. Lowest Common Ancestor of a Binary Tree (Medium) ](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

[108. Convert Sorted Array to Binary Search Tree (Easy)](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

[109. Convert Sorted List to Binary Search Tree (Medium)](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/)

[653. Two Sum IV - Input is a BST (Easy)](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)

[530. Minimum Absolute Difference in BST (Easy)](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/)

[501. Find Mode in Binary Search Tree (Easy)](https://leetcode.com/problems/find-mode-in-binary-search-tree/description/)

### Trie

[208. Implement Trie (Prefix Tree) (Medium)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

[677. Map Sum Pairs (Medium)](https://leetcode.com/problems/map-sum-pairs/description/)

## 栈和队列

[232. Implement Queue using Stacks (Easy)](https://leetcode.com/problems/implement-queue-using-stacks/description/)

[225. Implement Stack using Queues (Easy)](https://leetcode.com/problems/implement-stack-using-queues/description/)

[155. Min Stack (Easy)](https://leetcode.com/problems/min-stack/description/)

[20. Valid Parentheses (Easy)](https://leetcode.com/problems/valid-parentheses/description/)

[739. Daily Temperatures (Medium)](https://leetcode.com/problems/daily-temperatures/description/)

[503. Next Greater Element II (Medium)](https://leetcode.com/problems/next-greater-element-ii/description/)

## 哈希表

[1. Two Sum (Easy)](https://leetcode.com/problems/two-sum/description/)

[217. Contains Duplicate (Easy)](https://leetcode.com/problems/contains-duplicate/description/)

[594. Longest Harmonious Subsequence (Easy)](https://leetcode.com/problems/longest-harmonious-subsequence/description/)

[128. Longest Consecutive Sequence (Hard)](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## 字符串
[242. Valid Anagram (Easy)](https://leetcode.com/problems/valid-anagram/description/)

[409. Longest Palindrome (Easy)](https://leetcode.com/problems/longest-palindrome/description/)

[205. Isomorphic Strings (Easy)](https://leetcode.com/problems/isomorphic-strings/description/)

[647. Palindromic Substrings (Medium)](https://leetcode.com/problems/palindromic-substrings/description/)

[9. Palindrome Number (Easy)](https://leetcode.com/problems/palindrome-number/description/)

[696. Count Binary Substrings (Easy)](https://leetcode.com/problems/count-binary-substrings/description/)

## 数组与矩阵

[283. Move Zeroes (Easy)](https://leetcode.com/problems/move-zeroes/description/)

[566. Reshape the Matrix (Easy)](https://leetcode.com/problems/reshape-the-matrix/description/)

[485. Max Consecutive Ones (Easy)](https://leetcode.com/problems/max-consecutive-ones/description/)

[240. Search a 2D Matrix II (Medium)](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)

[378. Kth Smallest Element in a Sorted Matrix ((Medium))](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/)

[645. Set Mismatch (Easy)](https://leetcode.com/problems/set-mismatch/description/)

[287. Find the Duplicate Number (Medium)](https://leetcode.com/problems/find-the-duplicate-number/description/)

[667. Beautiful Arrangement II (Medium)](https://leetcode.com/problems/beautiful-arrangement-ii/description/)

[697. Degree of an Array (Easy)](https://leetcode.com/problems/degree-of-an-array/description/)

[766. Toeplitz Matrix (Easy)](https://leetcode.com/problems/toeplitz-matrix/description/)

[565. Array Nesting (Medium)](https://leetcode.com/problems/array-nesting/description/)

[769. Max Chunks To Make Sorted (Medium)](https://leetcode.com/problems/max-chunks-to-make-sorted/description/)

## 图

### 二分图

[785. Is Graph Bipartite? (Medium)](https://leetcode.com/problems/is-graph-bipartite/description/)

### 拓扑排序

[207. Course Schedule (Medium)](https://leetcode.com/problems/course-schedule/description/)

[210. Course Schedule II (Medium)](https://leetcode.com/problems/course-schedule-ii/description/)

### 并查集

[684. Redundant Connection (Medium)](https://leetcode.com/problems/redundant-connection/description/)

## 位运算

[461. Hamming Distance (Easy)](https://leetcode.com/problems/hamming-distance/)

[136. Single Number (Easy)](https://leetcode.com/problems/single-number/description/)

[268. Missing Number (Easy)](https://leetcode.com/problems/missing-number/description/)

[260. Single Number III (Medium)](https://leetcode.com/problems/single-number-iii/description/)

[190. Reverse Bits (Easy)](https://leetcode.com/problems/reverse-bits/description/)

[231. Power of Two (Easy)](https://leetcode.com/problems/power-of-two/description/)

[342. Power of Four (Easy)](https://leetcode.com/problems/power-of-four/)

[693. Binary Number with Alternating Bits (Easy)](https://leetcode.com/problems/binary-number-with-alternating-bits/description/)

[476. Number Complement (Easy)](https://leetcode.com/problems/number-complement/description/)

[371. Sum of Two Integers (Easy)](https://leetcode.com/problems/sum-of-two-integers/description/)

[318. Maximum Product of Word Lengths (Medium)](https://leetcode.com/problems/maximum-product-of-word-lengths/description/)

[338. Counting Bits (Medium)](https://leetcode.com/problems/counting-bits/description/)
