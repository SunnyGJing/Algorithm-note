1. 一次性导入多个模块
   ```python
    """
    __init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。

    通常__init__.py 文件为空，但是我们还可以为它增加其他的功能。我们在导入一个包时，实际上是导入了它的__init__.py文件。这样我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。
    """

    # package
    # __init__.py
    import re
    import urllib
    import sys
    import os

    # a.py
    import package 
    print(package.re, package.urllib, package.sys, package.os)

    ## 如果__init__.py中导入的是自定义的.py文件
    ## 那么这些.py会执行，.py中对应的变量会存储在内存中

    ##  ----------以下为示例--------------------------

    ## 例如datasets文件夹下
    ## ./datasets/__init__.py
    from .load_dataset import *

    ## ./datasets/load_dataset.py
    train_datasets = ...
    train_dataloader = torch.utils.data.DataLoader(train_datasets, 
                                                   batch_size=batch_size, 
                                                   shuffle=True, 
                                                   num_workers=2)

    ## 我们要运行的train.py，可以这样写
    from datasets import train_datasets, train_dataloader
    ```