from transformers import pipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

READER_MODEL_NAME = "Qwen/Qwen2-0.5B-Instruct" # for demo purposes, we use a smaller model

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")


# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_use_double_quant=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_compute_dtype=torch.bfloat16,
# )
model = AutoModelForCausalLM.from_pretrained(READER_MODEL_NAME, torch_dtype=torch.bfloat16).to(device)
tokenizer = AutoTokenizer.from_pretrained(READER_MODEL_NAME)

reader = pipeline(
    model=model,
    tokenizer=tokenizer,
    task="text-generation",
    device=device.index if device.type == 'mps' else -1,  # 確保使用 MPS 設備
    do_sample=True,
    temperature=0.2,
    repetition_penalty=1.1,
    return_full_text=False,
    max_new_tokens=500,
)
