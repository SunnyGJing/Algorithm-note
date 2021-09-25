1. 组batch
   ```python
    from torch.utils.data import Dataset, DataLoader
    
    class xxxx(Dataset):
		def __init__(self, ....):
            pass
		def __getitem__(self, index):
            pass
		def __len__(self):
            pass
    
    dataset = xxxxx(....)
    dataloader = DataLoader(dataset,
                            batch_size,
                            shuffle=(mode == 'train'), 
                            drop_last=False,
                            num_workers=n_jobs,
                            pin_memory=True
                            )
   ```