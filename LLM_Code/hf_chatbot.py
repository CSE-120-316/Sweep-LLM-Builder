# Rohit Rao April 4th, 2024
# Description: Basic inference code for interacting with finetuned model with PEFT.

import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments, pipeline, logging
from peft import LoraConfig, AutoPeftModelForCausalLM
from trl import SFTTrainer
import gc
from huggingface_hub import login

print("Torch Availability: ",torch.cuda.is_available()) # ignore

login(token='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') # my token to for access to meta llama 2 if needed

gc.collect()

new_model = "llama-2-7b-chat-hfmlabonne/guanaco-llama2-1k"
# Default: llama-2-7b-chat-hf, just need to add the datasetname to access the model.

# 4-bit Quantization Configuration
compute_dtype = getattr(torch, "float16")
quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=compute_dtype, bnb_4bit_use_double_quant=False)


# Load model with 4-bit precision
model = AutoPeftModelForCausalLM.from_pretrained(new_model, quantization_config=quant_config, device_map={"": 0})
model.config.use_cache = False
model.config.pretraining_tp = 1


# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(new_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"


# Set PEFT Parameters
peft_params = LoraConfig(lora_alpha=16, lora_dropout=0.1, r=64, bias="none", task_type="CAUSAL_LM")

# Force clean the pytorch cache
gc.collect()
torch.cuda.empty_cache()

# Test the model
while True:
    userinp = input("Enter 'finished' when you're finished: \n")
    if userinp.lower() == "finished":
        print("Thanks for using this chatbot.")
        break
    else:
        logging.set_verbosity(logging.CRITICAL)
        prompt = userinp
        pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=300)
        result = pipe(f" <s>[INST] {prompt} [/INST]")
        print(result[0]['generated_text'],"\n")
















