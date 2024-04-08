## YOLOX: Quick tool for running some object detection experiments.

Original repo and `yolox_s.pth` location: [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)


## How to run

- Convert your dataset in coco format.

```
  - dataset_directory/
    - images/
     - image1.jpg
     - abcfdtD.jpg
     - ...
    - annotations/
      - train_coco.json
      - val_coco.json
```

- Modify `exps/yolox_s_logy.py` 

- OR you can also run `python pipeline/setup.py` after modifying `pipeline/config.json`


- Run `./train_pipeline.sh` to train the file