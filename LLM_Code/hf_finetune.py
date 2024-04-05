# Rohit Rao April 4th, 2024
# Description: Basic inference code for interacting with finetuned model.
import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments, pipeline, logging
from peft import LoraConfig
from trl import SFTTrainer
import gc
from huggingface_hub import login

# torch check
print("Torch Availability: ",torch.cuda.is_available()) # ignore

login(token='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') # My key to access official llama2.

# Force garbage collection
gc.collect()
 

# Define model, dataset, and new model name
base_model = "meta-llama/Llama-2-7b-chat-hf" # Official Meta Llama2
datasetName = "AdiOO7/llama-2-finance"
# Working Datasets:
# "AdiOO7/llama-2-finance"
# "mlabonne/guanaco-llama2-1k"

new_model = "llama-2-7b-chat-hf" + datasetName


dataset = load_dataset(datasetName, split="train")


compute_dtype = getattr(torch, "float16")
quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=compute_dtype, bnb_4bit_use_double_quant=False)


model = AutoModelForCausalLM.from_pretrained(base_model, quantization_config=quant_config, device_map={"": 0})
model.config.use_cache = False
model.config.pretraining_tp = 1


tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"


peft_params = LoraConfig(lora_alpha=16, lora_dropout=0.1, r=64, bias="none", task_type="CAUSAL_LM")

outputdir = "./results/" + datasetName

training_params = TrainingArguments(output_dir=outputdir, num_train_epochs=1, per_device_train_batch_size=4, gradient_accumulation_steps=1, optim="paged_adamw_32bit", save_steps=25, logging_steps=25, learning_rate=2e-4, weight_decay=0.001, fp16=False, bf16=False, max_grad_norm=0.3, max_steps=-1, warmup_ratio=0.03, group_by_length=True, lr_scheduler_type="constant", report_to="tensorboard")

trainer = SFTTrainer(model=model, train_dataset=dataset, peft_config=peft_params, dataset_text_field="text", max_seq_length=None, tokenizer=tokenizer, args=training_params, packing=False)


gc.collect()
torch.cuda.empty_cache()


trainer.train()


trainer.model.save_pretrained(new_model)
trainer.tokenizer.save_pretrained(new_model)


logging.set_verbosity(logging.CRITICAL)
prompt = "Who is Pablo Picasso? Explain to me in Spanish (es)."
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200)
result = pipe(f" <s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])


