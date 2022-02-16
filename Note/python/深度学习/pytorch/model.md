1. 保存和加载整个网络结构和模型参数
    - `torch.save()`: 保存一个序列化的对象到磁盘，使用的是Python的pickle库来实现的。
    - `torch.load()`: 解序列化一个pickled对象并加载到内存当中。
    - `torch.nn.Module.load_state_dict()`: 加载一个解序列化的state_dict对象
    
    ```python
    torch.save(model, 'saved_model.pth')

    ## cpu
    model = torch.load('saved_model.pth', map_location='cpu')
    ## gpu
    model = torch.load('saved_model.pth')
    ```
2. 只保存和加载模型参数（推荐使用）
    ```python
    torch.save(model.state_dict(), 'saved_param.pth')

    model = TheModelClass(*args, **kwargs)
    model.load_state_dict(torch.load('saved_param.pth'))
    ```
3. 保存和加载带checkpoint的模型用于inference或resuming training
   ```python
    ## save
    torch.save({'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': loss,
                ...}, PATH)
    
    ## load
    model = TheModelClass(*args, **kwargs)
    optimizer = TheOptimizerClass(*args, **kwargs)

    checkpoint = torch.load(PATH)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoin['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']
   ```
4. 保存多个模型到一个文件中
   ```python
    ## save
    torch.save({'modelA_state_dict': modelA.state_dict(),
                'modelB_state_dict': modelB.state_dict(),
                'optimizerA_state_dict': optimizerA.state_dict(),
                'optimizerB_state_dict': optimizerB.state_dict(),
                ...}, PATH)

    ## load
    modelA = TheModelAClass(*args, **kwargs)
    modelB = TheModelAClass(*args, **kwargs)
    optimizerA = TheOptimizerAClass(*args, **kwargs)
    optimizerB = TheOptimizerBClass(*args, **kwargs)

    checkpoint = torch.load(PATH)
    modelA.load_state_dict(checkpoint['modelA_state_dict']
    modelB.load_state_dict(checkpoint['modelB_state_dict']
    optimizerA.load_state_dict(checkpoint['optimizerA_state_dict']
    optimizerB.load_state_dict(checkpoin['optimizerB_state_dict']
   ```
5. 双显卡并行
   ```python
    device_ids = range(torch.cuda.device_count())
    model = torch.nn.DataParallel(model, device_ids=device_ids)

    ## model不再是model，而是model.module
    model.module.generate()
   ```
6. torch.cuda 获取显卡信息
   ```python
   device = 'cuda' if torch.cuda.is_available() else 'cpu'
   ```
7. 搭建模型
   ```python
    import torch.nn as nn
    
    class Net(nn.Module):
            def __init__:
                super(Net, self).__init__()
            def forward:
                pass
            def cal_loss:
                pass

    model = Net(.....).to(device)
   ```

8. 以batch为单位，反向传播 & 梯度更新
   ```python
    """
    1. optimizer.zero_grad()
        以batch为单位反向传播，计算新的batch的梯度时，要先把梯度清零，否则两个batch的梯度值会累加起来
    2. loss.backward()
        Pytorch的autograd自动沿着计算图反向传播，计算链式法则求导之后的结果值
    3. optimizer.step()
        更新参数，例如参数w和b更新操作
    """

    # optimizer = torch.optim.Adam(...)
    optimizer = torch.optim.SGD(model.parameters(),
                                lr=3e-4,
                                momentum=0.9,
                                weight_decay=1e-5)
    
    # making sure to ignore the loss on <pad> tokens.
    # criterion = nn.CrossEntropyLoss(ignore_index=0)
    loss = nn.MSELoss()(out, labels)
    
    CosineDecayLR(optimizer,
                  T_max=epochs * len(train_loader),
                  lr_init=lr,
                  lr_min=1e-9,
                  warmup=5 * len(train_loader))

    optimizer.zero_grad()  ## 清空梯度信息
    loss.backward()  ## loss反向传播
    optimizer.step()  ## 参数的梯度更新
   ```