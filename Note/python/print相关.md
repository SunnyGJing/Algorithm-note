1. pytorch完整打印所有元素（不要省略号）
   ```
   torch.set_printoptions(threshold=np.inf)
   ```
2. pytorch打印时精确到小数点后5位
   ```
   torch.set_printoptions(precision=5)
   ```
3. pytorch打印时不使用以e为底数的科学计数法
   ```
   torch.set_printoptions(sci_mode=False)
   ```