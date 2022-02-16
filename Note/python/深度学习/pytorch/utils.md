1. 组batch
   ```python
   from torch.utils.data import Dataset, DataLoader
   
   class DatasetName(Dataset):
      def __init__(self, data):
            self.x = torch.from_numpy(data[:, 0:-1])
            self.y = torch.from_numpy(data[:, -1])
            self.length = len(data)

      def __getitem__(self, index):
            return self.x[index], self.y[index]
      
      def __len__(self):
            return self.length
   dataset = DatasetName(data)
   dataloader = DataLoader(dataset,
                            batch_size,
                            shuffle=(mode == 'train'), 
                            drop_last=False,
                            num_workers=n_jobs,
                            pin_memory=True)
   ```