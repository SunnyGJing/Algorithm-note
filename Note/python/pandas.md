1. 打印信息显示不完整
    ```python
    # 很卡噢，谨慎使用

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    #设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth',100)
    ```

2. 修改列标题
   ```python
    print(dataframe.columns)
    print(dataframe.index)

    # 修改列标题id为test_id
    DataFrame.rename(columns={'id':'test_id'}, inplace=True)
    ```

3. 选择某行、某列  
    ```python
    dataframe.loc[:, ('file_id', 'label')]
    dataframe.iloc[:, 1]
    ```

4. 删除某列/多列
   ```python
   # 删除一列
   DataFrame.drop('label', axis=1)

   # 删除多列
   DataFrame.drop(['xxx', 'yyy'], axis=1)
   ```
5. 删除含缺失值的行/列
    ```python
    DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

    """
    axis=0 / 1: 删除包含缺失值（NaN）的行 / 列
    how='any' / 'all', 出现一个Nan就删除 / 全部Nan才删除
    subset 只检查部分行/列
    """

    f_data = f_raw.dropna(axis=0, how='any')
    ```

6. 插入列
   ```python
   # 插入列作为第1列，列标题为prob_1，填充值为0.125
    DataFrame.insert(1, 'prob_1', 0.125)
   ```
7. 一行变多行
   ```python
    ## pandas>=0.25
    # 先将字段拆分
    df['xxx']=df['xxx'].str.split(',')
    # 调用explode()方法 
    df.explode('xxx')
   ```
8. 修改特定列的内容
    ```python
    # 用一个数字为指定行/列赋值
    Y_sample.loc[:, 'price'] = 0
    
    # 修改某列的内容
    f_data['服务'].apply(lambda x: '{}。{}'.format(x.split('→')[2], x.split('→')[5]))

    # 两列的内容合并为一列
    f_data[['客户','客服']].apply(lambda x:''.join(x), axis=1)

    # 修改某列的字符串内容
    f_data['qa_text'].str.replace(';', '')

    # 通过处理某列的字符串内容 筛选部分数据
    f_data[f_data['服务'].str.split('→').apply(lambda x: len(x)) >= 6]

    # 删除某列中符合特定值的行
    f_data[~(f_data['服务']=='其他')]
    ```

9.  读取文件
    ```python
    # csv文件、tsv文件
    pd.read_csv('xxx.csv')

    # excel文件，skiprows用于跳过前几行
    pd.read_excel('xxx.xlsx',
                  skiprows=[0],
                  usecols=['xxx','yyy'],
                  dtype=str)
    ```

10. 保存文件
    ```python
    DataFrame.to_csv('file_name', sep='\t', encoding=;utf-8, index=False, header=False)
    ```