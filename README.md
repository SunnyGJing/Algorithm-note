## 一、题目简记
```
便于快速复习
分别按类别和按题号排列

Note: 为了便于记忆，代码语法并不严谨
```
### 按类别整理：
#### 模式1：滑动窗口/动态规划
<details>
<summary>53.返回最大连续子数组(含负数)的和</summary>

方法：优化后的动态规划
```python
# 循环内
cur_val = nums[i]>0 ? cur_val+nums[i] : nums[i]
max_val = max(max_val, cur_val)

```
</details>
<details>

<summary>659.将有序数组拆为数值连续的子序列(长度>=3)</summary>

方法：用哈希表模拟多个单调队列
```python
# 初始化
hasht = collections.default(list)

# 数组遍历
pre_small = hasht.get(nums[i]-1, 0)
hasht[nums[i]].append(pre_small + 1)

hasht[nums[i]-1].remove(pre_small)

# 字典遍历
return False if i<3 for list in hasht.values() for i in list
```

</details>

<details>
<summary>1296.将无序数组拆为数值连续的子序列(长度=k)</summary>

方法：
```python
# 初始化
return False if len(nums) % k

count = collections.Counter(nums)

# 字典不为空时 循环
start = min(count.keys())

return False if count[num+i]<count[num] for i in range(1,k)
count[num+i] -= count[num] for i in reversed(range(k,-1))

```

</details>


## 二、刷题计划与记录
```
2020.02计划：
周中每天刷10道题  
周末不刷题，只做总结和复习

2020.03计划：
每天上午做总结和复习1小时刷题3小时  
```
### 2020年
#### 二月

<details>
<summary>2.12 Wed. 未分类 [7]</summary>

- [x] 1. Two Sum
- [x] 15. 3Sum
- [x] 26. Remove Duplicates from Sorted Array
- [x] 80. Remove Duplicates from Sorted Array II
- [x] 83. Remove Duplicates from Sorted List
- [x] 844. Backspace String Compare
- [x] 977. Squares of a Sorted Array

</details>  

<details>
<summary>2.13 Thur. 滑动窗口 [10/10] 已完成 </summary>

- [x] 82. Remove Duplicates from Sorted List II  
- [x] Google | Remove Duplicates from Unsorted Array
- [x] 316. Remove Duplicate Letters
- [x] 360. Sort Transformed Array
- [x] 16. 3Sum Closest
- [x] 259.ThreeSumSmaller
- [x] 713. Subarray Product Less Than K
- [x] 152. Maximum Product Subarray
- [x] 325. Maximum Size Subarray Sum Equals k
- [x] 560. Subarray Sum Equals K
</details>  

<details>
<summary>2.14 Fri. 有序数组多指针 [6/10]</summary>

- [x] 1099. Two Sum Less Than K
- [x] 198. House Robber
- [x] 213. House Robber II
- [x] 337. House Robber III
- [x] 256. Paint House
- [x] 265. paint house ii
- [ ] 238. Product of Array Except Self
- [ ] 628. Maximum Product of Three Numbers
- [ ] 974. Subarray Sums Divisible by K
- [ ] 75. Sort Colors
</details>

<details>
<summary>2.17 Mon. 快慢指针 [10/10] 已完成 </summary>

- [x] 141. Linked List Cycle
- [x] 142. Linked List Cycle II
- [x] 234. Palindrome Linked List
- [x] 457. Circular Array Loop
- [x] 918. Maximum Sum Circular Subarray
- [x] 202. Happy Number
- [x] 876. Middle of the Linked List
- [x] 143. Reorder List
- [x] 287. Find the Duplicate Number
- [x] 160. Intersection of Two Linked Lists
</details>

<details>
<summary>2.18 Tue. 快慢指针 [10/10] 已完成 </summary>

- [x] 206. Reverse Linked List
- [x] 92. Reverse Linked List II
- [x] 156. Binary Tree Upside Down
- [x] 268. Missing Number
- [x] 41. First Missing Positive
- [x] 136. Single Number
- [x] 263. Ugly Number
- [x] 258. Add Digits
- [x] 599. Minimum Index Sum of Two Lists
- [x] 645. Set Mismatch
</details>

#### 三月

<details>
<summary>3.17 Tues. 区间合并 [13] 好难啊啊啊梦魇(update：打败了梦魇)</summary>

- [x] 729. My Calendar I （判断某区间是否与其它区间重合）
- [x] 731. My Calendar II （判断某区间是否同时与其它k个区间重合）
- [x] 252. Meeting Rooms I  （判断多个区间中是否存在区间重合）
- [x] 253. Meeting Rooms II （多个区间的重合区间个数）
- [x] 732. My Calendar III （多个区间的重合区间个数）

- [x] 56. Merge Intervals 区间合并
- [x] 57. Insert Interval 区间插入
- [x] 986. Interval List Intersections 区间交集
- [x] 435. Non-overlapping Intervals 计算最小删区间个数使不重合

- [x] 218. The Skyline Problem 区间的附加属性值(e.g.第三维高度)
- [x] 621. Task Scheduler 最小化区间总长度(...)

- [ ] 207. Course Schedule 判断课程安排是否存在冲突？
- [ ] 636. Exclusive Time of Functions 计算每个区间的无重合长度
</details>

<details>
<summary> [0] </summary>

- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
</details>


