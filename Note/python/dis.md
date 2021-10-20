1. 用dis包查看多元素赋值的细节
   ```python
    import dis

    nums = [2,3,5,4,1]
    def test():
        j = 2
        # 下面两行得到不同的结果！
        nums[j], j = -1, nums[j]
        j, nums[j] = nums[j], -1
    
    dis.dis(test)
   ```