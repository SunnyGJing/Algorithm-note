1. model.load() 加载模型参数
    ```python
    ## cpu
    model = torch.load(model_path, map_location='cpu')
    ## gpu
    model = torch.load(model_path)
    ```
2. 双显卡并行
   ```python
    model = torch.nn.DataParallel(model, device_ids=[0,1])

    ## model不再是model，而是model.module
    model.module.generate()
   ```
3. torch.cuda 获取显卡信息
   ```python
   device = 'cuda' if torch.cuda.is_available() else 'cpu'
   ```
4. 搭建模型
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
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(),
                                 lr=0.0003, 
                                 weight_decay=1e-5)

    model = torch.nn.DataParallel(model, device_ids=[0,1])

    del model
    model = Net(...)
    ckpt = torch.load(config['best_model_dir'],
                      map_location='cpu')
    model.load_state_dict(ckpt)
   ```