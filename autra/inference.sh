torchrun --standalone --nproc_per_node 2 scripts/inference.py configs/opensora/inference/64x512x512.py --ckpt-path OpenSora-v1-HQ-16x512x512.pth --prompt-path ./assets/texts/t2v_samples.txt