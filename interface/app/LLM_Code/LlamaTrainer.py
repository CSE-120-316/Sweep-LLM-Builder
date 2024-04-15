# Rohit Rao
# Llama2 Finetuner Object.
# 4/12/2024

#
import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments, pipeline, logging
from peft import LoraConfig, AutoPeftModelForCausalLM
from trl import SFTTrainer
import gc
from huggingface_hub import login
#

#
class LlamaTrainer:
    def __init__ (self, newModel = "", dataSet = "", learningRate = ""): # 2e-4
        self.newModel = newModel
        self.dataSet = dataSet
        self.learningRate = learningRate
    def trainLLM(self):

        print("DEFINED PARAMS:",self.newModel,self.dataSet,self.learningRate)
        # Login to Rohit HuggingFace Key:
        login(token='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') #  key to access official meta - llama2.
        gc.collect()
        #
        BASE = "meta-llama/Llama-2-7b-chat-hf"
        # Loading Local Dataset
        local_dataset = load_dataset("json", data_files=self.dataSet, split="train")
        compute_dtype = getattr(torch, "float16")
        quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=compute_dtype, bnb_4bit_use_double_quant=False)
        model = AutoModelForCausalLM.from_pretrained(BASE, quantization_config=quant_config, device_map={"": 0})
        model.config.use_cache = False
        model.config.pretraining_tp = 1
        # Using autotokenizer from hf for simplicity
        tokenizer = AutoTokenizer.from_pretrained(BASE, trust_remote_code=True)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "right"
        peft_params = LoraConfig(lora_alpha=16, lora_dropout=0.1, r=64, bias="none", task_type="CAUSAL_LM")
        outputdir = "./results/" + self.dataSet
        training_params = TrainingArguments(output_dir=outputdir, num_train_epochs=1, per_device_train_batch_size=4, gradient_accumulation_steps=1, optim="paged_adamw_32bit", save_steps=25, logging_steps=25, learning_rate=2e-4, weight_decay=0.001, fp16=False, bf16=False, max_grad_norm=0.3, max_steps=-1, warmup_ratio=0.03, group_by_length=True, lr_scheduler_type="constant", report_to="tensorboard")
        trainer = SFTTrainer(model=model, train_dataset=local_dataset, peft_config=peft_params, dataset_text_field="text", max_seq_length=None, tokenizer=tokenizer, args=training_params, packing=False)
        gc.collect()
        torch.cuda.empty_cache()
        trainer.train()
        trainer.model.save_pretrained(self.newModel)
        trainer.tokenizer.save_pretrained(self.newModel)
