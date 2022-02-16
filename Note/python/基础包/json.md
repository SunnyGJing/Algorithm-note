1. load 和 loads
   ```python
    # 从json文件读取dict
    json.load(open('file.json', 'r'))

    # 字符串转dict
    json.loads('{"a": "1", "b": "2"}')
   ```

2. dump 和 dumps
   ```python
    # 把dict写入json文件
    json.dump(dict_1, open('file.json', 'w'))

    # dict转字符串
    json.dumps(dict_1)
   ```