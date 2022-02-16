1. 自定义比较函数
   ```
    from functools import cmp_to_key
    nums.sort(key=cmp_to_key(lambda x,y: 1 if x+y>y+x else -1))
    ## 注意key参数的规则：
    ## 如果得到的值小于0，则交换值。如果值大于等于0，则不执行任何操作
   ```