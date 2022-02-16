1. 划分数据集
```python
from sklearn.model_selection import train_test_split

# 非随机划分
train, dev = train_test_split(f_data, test_size=0.1, shuffle=False)

# 随机划分
train, dev = train_test_split(f_data, test_size=0.1, random_state=2021)

# 保持数据分布的随机划分
train, dev = train_test_split(f_data, test_size=0.1, random_state=2021, stratify=f_data['label'])
```