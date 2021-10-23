"""
while True:
    n = input().strip()
    if n != '':
        lens = list(map(int, input().strip().split(' ')))
        lens.sort()
        n = len(lens)
        a, b, c, flag = 0, 1, 2, False
        while c < n:
            if lens[a] + lens[b] > lens[c]:
                flag = True
                break
            else:
                a, b, c = a+1, b+1, c+1
        if flag: print('possible')
        else: print('impossible')
    else:
        break
"""

"""
求数列的和

（编程题须知）（参考答案）

时间限制： 4000MS
内存限制： 557056KB
题目描述：
数列的定义如下： 数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。


输入描述
输入数据有多组，每组占一行，由两个整数n（n<10000）和m(m<1000)组成，n和m的含义如前所述。

输出描述
对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。


样例输入
81 4
2 2

样例输出
94.73
3.41
"""
# import math
#
# while True:
#     n = input().strip()
#     if n != '':
#         nums = list(map(int, n.split(' ')))
#         n, m, res = nums[0], nums[1], 0
#         for i in range(m):
#             res += n
#             n = math.sqrt(n)
#         print("%.2f" % res)
#     else:
#         break


"""
水仙花数

（编程题须知） （参考答案） 

时间限制： 4000MS
内存限制： 557056KB
题目描述：
春天是鲜花的季节，水仙花就是其中最迷人的代表，数学上有个水仙花数，他是这样定义的： 
“水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，
比如：153=1^3+5^3+3^3。 现在要求输出所有在m和n范围内的水仙花数。



输入描述
输入数据有多组，每组占一行，包括两个整数m和n（100<=m<=n<=999）。

输出描述
对于每个测试实例，要求输出所有在给定范围内的水仙花数，
就是说，输出的水仙花数必须大于等于m,并且小于等于n，
如果有多个，则要求从小到大排列在一行内输出，之间用一个空格隔开; 
如果给定的范围内不存在水仙花数，则输出no; 每个测试实例的输出占一行。


样例输入
100 120
300 380

样例输出
no
370 371
"""


# while True:
#     n = input().strip()
#     if n != '':
#         nums = list(map(int, n.split(' ')))
#         start, end, res = nums[0], nums[1], []
#         for i in range(start, end+1):
#             if i == sum([int(s) * int(s) * int(s) for s in str(i)]):
#                 res.append(str(i))
#         if res:
#             print(' '.join(res))
#         else:
#             print('no')
#     else:
#         break


"""
数字变换
时间限制： 3000MS
内存限制： 589824KB

题目描述：
Kimi今天在玩一个数字变换游戏。游戏规则如下： 
首先给出N个数字0。 
然后开始从数字S开始报数，当报数为S时，将所有出现在S以及S的倍数位置的0变成1（位置编号从1开始），
当所有S及S倍数位置的数字都变换之后即完成了一趟数字变换。 
接下来报数S+1，将所有出现在S+1以及S+1的倍数位置的数字进行一次变换。
如果原来数字为0，则变成1；如果原来数字为1，则变成0。 
接下来报数S+2，相应的也需要将所有出现在S+2以及S+2的倍数位置的数字进行一次变换。
如果原来数字为0，则变成1；如果原来数字为1，则变成0。 ...... 
当报数为数字T（T>S）时，将所有T以及T的倍数位置的数字都进行一次变换。
如果原来数字为0，则变成1；如果原来数字为1，则变成0。 
请问在报数T结束，且所有对应位置的数字都变换后，所有的数字中一共有多少个1？



输入描述
单组输入。 输入三个正整数N、S和T。N<=1000，1<=S<T<=N 从S开始报数直到T结束，包含S和T。

输出描述
输出变换之后，在所有的数字中最终包含的1的个数。


样例输入
10 1 10
样例输出
3
"""

# while True:
#     inp = input().strip()
#     if inp != '':
#         nums = list(map(int, inp.split(' ')))
#         n, s, t = nums[0], nums[1], nums[2]
#         dp = [0] * (n + 1)
#         for j in range(s, t+1):
#             cur = j
#             while cur <= n:
#                 dp[cur] = 0 if dp[cur] == 1 else 1
#                 cur += j
#         print(dp.count(1))
#     else:
#         break


"""
6.
挖掘宝石
时间限制： 3000MS
内存限制： 589824KB

题目描述：
小明设计了一个挖掘宝石的小游戏。在游戏中有红宝石、蓝宝石、绿宝石等多种不同类型的宝石，当然也有昂贵的钻石。 
现在给出一个地图，在地图上有N种不同的宝石。每一种宝石都有一颗或者多颗，同一种宝石每一颗的价值都是相同的。 
此外，每一种宝石都有一个挖掘时间。 在给定的时间内，哪一个玩家挖掘的宝石的总价值最大就是游戏的赢家。 
现在给出N类不同宝石的数量以及每一类宝石中每一颗的价值和挖掘时间，并且给出一个总的游戏时间T。
在不考虑竞争对手的情况下，请问可以得到的最大价值是多少？

输入描述
单组输入。 第1行输入一个正整数N和一个正整数T，分别表示宝石类型的数量和总游戏时间（分钟），
两者之间用空格隔开。N<=100，T<=1000。 
从第2行到第N+1行每一行三个正整数X[i]，Y[i]和Z[i]，
分别表示第i类宝石的数量、第i类宝石中一颗宝石的价值和挖掘时间（分钟）。
X[i]、Y[i]和Z[i]均不超过100。

输出描述
输出可以得到的最大价值。

样例输入
3 10
2 5 5
3 4 3
2 8 6

样例输出
12
"""

while True:
    n = input().strip()
    if n != '':
        NT = list(map(int, input().strip().split(' ')))
        n, t = NT[0], NT[1]
        v, w, c = [], [], 0
        for i in range(n):
            XYZ = list(map(int, input().strip().split(' ')))
            x, y, z = XYZ[0], XYZ[1], XYZ[2]
            v.extend([y] * x)
            w.extend([z] * x)
            c += x
        tmp = [[0 for _ in range(t+1)] for j in range(c+1)]
        for i in range(1, c+1):
            for j in range(1, t+1):
                tmp[i][j] = tmp[i-1][j]
                if j >= w[i-1] and tmp[i][j] < tmp[i-1][j-w[i-1]] + v[i-1]:
                    tmp[i][j] = tmp[i-1][j-w[i-j]] + v[i-1]
        print(tmp[-1][-1])

    else:
        break



"""
3.
木箱子
时间限制： 3000MS
内存限制： 589824KB

题目描述：
现在有很多木箱子，每一个箱子都是标准的长方体并且都是空心的。
如果一个木箱子的长、宽和高都大于（不能等于）另一个木箱子，则小的箱子可以套到大的箱子里面。
（注意：此处不考虑材质本身的厚度，且每一个木箱子在嵌套的时候长、宽、高都不允许旋转）

现在告诉你一些长方体木箱子的长、宽和高，请问这些木箱子最多可以嵌套多少层？

输入描述
单组输入。

第1行输入一个正整数N，表示长方体木箱子的总数量。(N<=1000)

接下来N行每行包含三个正整数，两两之间用空格隔开，分别表示每一个长方体木箱子的长、宽和高。（长、宽、高均小于等于10000。）

输出描述
输出一个正整数，表示木箱子最多可以嵌套的层数。


样例输入
4
1 2 3
3 6 3
2 3 4
3 4 5

样例输出
3
"""
[354. 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes/)
[面试题 08.13. 堆箱子](https://leetcode-cn.com/problems/pile-box-lcci/)
# while True:
#     n = input().strip()
#     if n != '':
#         n = int(n)
#         dp = [[(float('inf'), float('inf'), float('inf')),
#                (float('-inf'), float('-inf'), float('-inf')), 0] for i in range(n)]
#         for i in range(n):
#             abc = sorted(list(map(int, input().strip().split(' '))))
#             a, b, c = abc[0], abc[1], abc[2]
#             dp[i] = [(a,b,c),(a,b,c),1]
#             for j in range(i):
#                 min_a, min_b, min_c, max_a, max_b, max_c, cnt = \
#                         dp[j][0][0], dp[j][0][1], dp[j][0][2], \
#                         dp[j][1][0], dp[j][1][1], dp[j][1][2], dp[j][2]
#                 if cnt >= dp[i][2] and a < min_a and b < min_b and c < min_c:
#                     dp[i] = [(a,b,c),(max_a,max_b,max_c),cnt+1]
#                 elif cnt >= dp[i][2] and a > max_a and b > max_b and c > max_c:
#                     dp[i] = [(min_a,min_b,min_c),(a,b,c),cnt+1]
#         res = 0
#         for i in range(n):
#             res = max(res, dp[i][2])
#         print(res)
#     else:
#         break




"""
1.
草船借箭
时间限制： 3000MS
内存限制： 589824KB

题目描述：
程序员小周同学这几天在看《三国演义》。今天他看到了“草船借箭”这一回，在钦佩诸葛亮巧借东风向曹操“借”箭的同时，
小周想到这么一个问题： 如果诸葛亮一共派出了N条放置草人的船来“借”箭。
“慷慨”的曹操向第1条草船上射了A支箭、第2条草船上射了B支箭，第3条草船上射的箭的数量等于前面两条船上箭的数量之和多一支，
第4条草船上射的箭的数量等于前面三条船上的箭的数量之和多一支，......，
以此类推，第N条草船上箭的数量等于前面N-1条船上箭的数量之和多一支。 
下面问题来了，请问这一次诸葛亮一共从曹操那里“借”了多少支箭呢？

输入描述
单组输入。 输入三个正整数N、A和B，三个正整数都不超过1000，并且保证N>1，且两两之间用空格隔开。

输出描述
输出诸葛亮“借”箭的总数量，结果对1e9+7取模。

样例输入
4 1 2
样例输出
15
"""
# while True:
#     NAB = input().strip()
#     if NAB != '':
#         nab = list(map(int, NAB.split(' ')))
#         n, a, b = nab[0], nab[1], nab[2]
#         if n == 1:
#             print(a)
#         elif n == 2:
#             print(a + b)
#         else:
#             res, ct = 0, 1
#             for i in range(2, n):
#                 res += ct
#                 ct *= 2
#             res = (a + b + 1) * res + a + b
#             print(res % 1000000007)
#     else:
#         break


"""
4.
二叉树
时间限制： 3000MS
内存限制： 589824KB
题目描述：
小明同学这段时间在学习数据结构中的二叉树。
一天，他遇到一个这样的问题： 有一棵满二叉树，从根结点开始每一个结点都拥有一个编号，
根结点的编号是1，其左子结点编号为2，右子结点编号为3，以此类推，从上至下、从左至右逐个按顺序为结点编号。 
现在为每个结点再增加一个正整数权重值，然后输入一个查询结点的编号，
计算以该结点作为根结点的左子树所有结点和右子树所有结点的权重和。
如果左子树的权重和大于右子树的权重和，输出“”，
如果右子树的权重和大于左子树的权重和，输出“”，
如果左、右子树的权重和相等，则输出“”。
如果待查询结点是叶子结点也输出“"。 
请编写一个程序实现上述功能。

输入描述
第1行输入二叉树的总结点个数N，N<=1000。 
第2行输入二叉树上N个结点每一个结点的权重值，两个权重值之间用英文空格隔开，按照从上至下，从左至右的顺序依次给出每个结点的权重值。

第3行输入待查询结点的编号（输入的编号<=N）。

输出描述
按照题目要求输出指定的字符。以输入的待查询结点为根结点，如果左子树的权重和大于右子树的权重和，输出“L”，如果右子树的权重和大于左子树的权重和，输出“R”，如果左、右子树的权重和相等，则输出“E”。如果待查询结点是叶子结点也输出“E"。


样例输入
7
1 2 3 3 2 5 1
3
样例输出
L
"""

# while True:
#     n = input().strip()
#     if n != '':
#         n = int(n)
#         nums = list(map(int, input().strip().split(' ')))
#         target = int(input().strip())
#         def helper(x):
#             if x > n: return 0
#             return nums[x-1] + helper(x*2) + helper(x*2+1)
#         l, r = target * 2, target * 2 + 1
#         sum_l, sum_r = helper(l), helper(r)
#         if sum_l > sum_r: print('L')
#         elif sum_l < sum_r: print('R')
#         else: print('E')
#     else:
#         break














