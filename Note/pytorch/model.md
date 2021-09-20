1. model.load
```python
## cpu
model = torch.load(model_path, map_location='cpu')
## gpu
model = torch.load(model_path)
```