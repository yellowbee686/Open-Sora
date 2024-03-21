from transformers import AutoModel, AutoTokenizer

# model_name = "bigcode/starcoder2-7b"
model_name = "DeepFloyd/t5-v1_1-xxl"
cache_dir = "/work02/chengxiao/cache_dir"
model = AutoModel.from_pretrained(model_name, cache_dir=cache_dir)
# tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)