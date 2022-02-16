1. 获取token id的三种方法
   ```python
    from transformers import BertTokenizer
    
    tokenizer = BertTokenizer.from_pretrained('hfl/chinese-bert-wwm-ext')
    
    ## 如下两种写法等价
    # 写法 1
    tokenizer.encode("xxxx",add_special_tokens=False)
    # 写法 2
    seg=tokenizer.tokenize("xxxx")
    tokenizer.convert_tokens_to_ids(seg)

    ## 如上两种写法不返回只返回input_ids
    ## 如下写法以dict返回input_ids、attention_mask和token_type_ids
    # 写法 3
    tokenizer.encode_plus("xxxx",
                           return_token_type_ids=True,
                           return_attention_mask=True)

    ## 示例：按max_lenght补齐/截断文本的写法如下
    ## [CLS] + content + [SEP] + [PAD] ...
    token_ids = tokenizer.encode("xxxx",
                                 max_length=128,
                                 pad_to_max_length=True)
   ```
   示例代码如下：
   ```python
    from transformers import BertTokenizer, BertModel
    tokenizer = BertTokenizer.from_pretrained('hfl/chinese-bert-wwm-ext')
    content = '外面的天气怎么样？'
    print(tokenizer.tokenize(content))
    print(tokenizer.convert_tokens_to_ids(tokenizer.tokenize(content)))
    print(tokenizer.encode(content))
    print(tokenizer.encode(content, 
                        max_length=15,
                        pad_to_max_length=True))
    print(tokenizer.convert_ids_to_tokens(tokenizer.encode(content, 
                        max_length=15,
                        pad_to_max_length=True)))
    ```
    示例代码运行结果如下：
    ```
    ['外', '面', '的', '天', '气', '怎', '么', '样', '？']
    [1912, 7481, 4638, 1921, 3698, 2582, 720, 3416, 8043]
    [101, 1912, 7481, 4638, 1921, 3698, 2582, 720, 3416, 8043, 102]
    [101, 1912, 7481, 4638, 1921, 3698, 2582, 720, 3416, 8043, 102, 0, 0, 0, 0]
    ['[CLS]', '外', '面', '的', '天', '气', '怎', '么', '样', '？', '[SEP]', '[PAD]', '[PAD]', '[PAD]', '[PAD]']

    ```