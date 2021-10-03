1. 用list一次性写入多行
    ```python
    d = [..., ..., ..., ...]

    with open('xxx.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(d)
    ```
2. 用两个list一次性写入多行
    ```python
    c = [..., ..., ..., ...]
    d = [..., ..., ..., ...]

    with open('xxx.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(c, d))
    ```
3. 用'\t'分隔多列
    ```python
    with open('xxx.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
    ```