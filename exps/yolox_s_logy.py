#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os
from yolox.exp import LogyExp


class Exp(LogyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/logy-coco-format-dataset"
        self.train_ann = "train_coco.json"
        self.val_ann = "val_coco.json"

        self.train_name = "images"
        self.val_name = "images"

        self.num_classes = 1

        # self.max_epoch = 100
        self.data_num_workers = 4
        # self.eval_interval = 1

        #training config --
        #
        # epoch number used for warmup
        self.warmup_epochs = 5
        # max training epoch
        self.max_epoch = 300
        # minimum learning rate during warmup
        self.warmup_1r = 0
        self-min_Ir_ratio = 0.05
        # learning rate for one image. During training, Ir will multiply batchsize.
        self.basic_r_per_img = 0.01 / 64.0/
        # name of LRScheduler
        self. scheduler = "yoloxwarmcos"
        # last #epoch to close augmention like mosaic
        self.no_aug_epochs = 15
        # apply EMA during training
        self.ema = True
        # weight decay of optimizer
        self.weight_decay = 5€-4
        # momentum of optimizer
        self momentum = 0.9
        # log period in iter, for example,
        # if set to 1, user could see log every iteration.
        self.print_interval = 10
        # eval period in epoch, for example,
        # if set to 1, model will be evaluate after every epoch.
        self.eval_interval = 10
