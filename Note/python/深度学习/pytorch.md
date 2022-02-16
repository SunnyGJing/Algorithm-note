1. tensor拼接
   - cat
    ```python
    a1 = torch.rand(4,3,16,32)
    a2 = torch.rand(4,3,16,32)
    torch.cat([a1,a2],dim=2).shape
    # torch.Size([4, 3, 32, 32])
    ```
   - stack
    ```python
    a1 = torch.rand(4,3,16,32)
    a2 = torch.rand(4,3,16,32)
    torch.stack([a1,a2],dim=2).shape
    # torch.Size([4, 3, 2, 16, 32])
    ```