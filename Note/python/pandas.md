1. 打印信息显示不完整
```python
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
```

2.选择某行、某列
```python
dataframe.loc[:, ('file_id', 'label')]
```

3. 删除含缺失值的行/列
```python
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

#axis=0: 删除包含缺失值（NaN）的行
#axis=1: 删除包含缺失值（NaN）的列
## how='any', 出现一个Nan就删除
## how='all', 全部Nan才删除
```

4. 修改特定列的内容
```python
dataframe.apply(lambda x:)
```