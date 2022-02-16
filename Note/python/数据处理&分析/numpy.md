1. 随机数数组
   ```python
   pd.random.seed(2021)

   # shape=(3,)的数值在[1,10)区间内的整数ndarray
   x = pd.random.randint(1, 10, 3)

   # shape=(1,3)的数值在[1,10)区间内的整数ndarray
   x = pd.random.randint(1, 10, (1, 3))

   # shape=(3,)的数值在[0,1)区间内的小数ndarray
   x = pd.random.random(3)

   # shape=(1,3)的数值在[0,1)区间内的小数ndarray
   x = pd.random.random((1, 3))
   ```