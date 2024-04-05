# Toy example to fine-tune GPT

## Dataset
Extraction of every question/answers from the whole Molière's corpus. 
Data handling is done in `llm_lora` tiny lib.

## Goal 
Try to make an LM/LLM talk like molière

## Methods
- try_lora.ipynb applies LoRA fine-tuning technics on small LM (that fit into an M3Pro's RAM)
- fine-tune-on-gpt.ipynb prepares a dataset for OpenAI's fine-tuning framework