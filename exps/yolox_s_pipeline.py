import os
from yolox.exp import LogyExp

class Exp(LogyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.5
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define your dataset path
        self.data_dir = "datasets/new-dataset"
        self.train_ann = "train_split.json"
        self.val_ann = "val_split.json"

        self.train_name = "images"
        self.val_name = "images"

        self.num_classes = 1

        self.max_epoch = 100
        self.data_num_workers = 4

        self.eval_interval = 1