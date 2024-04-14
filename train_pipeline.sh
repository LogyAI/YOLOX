python tools/train.py -f exps/yolox_s_pipeline.py -d 1 -b 16 --fp16 -o -c yolox_s.pth --cache

# For converting .pth to onnx
python tools/export_onnx.py -f exps/yolox_s_pipeline.py --output-name pipeline_model_trained.onnx -n yolox-s -c YOLOX_outputs/yolox_s_pipeline/best_ckpt.pth