import os

import torch
from datasets import load_from_disk
from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer,
                          DataCollatorForSeq2Seq, Trainer, TrainingArguments)

from textSummarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        config = self.config

        device = "cuda" if torch.cuda.is_available() else "cpu"

        tokenizer = AutoTokenizer.from_pretrained(config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(
            config.model_ckpt).to(device)

        seq2seq_data_collator = DataCollatorForSeq2Seq(
            tokenizer, model=model_pegasus)

        dataset_pt = load_from_disk(config.data_path)

        training_args = TrainingArguments(
            output_dir=config.root_dir, num_train_epochs=config.num_train_epochs, warmup_steps=config.warmup_steps,
            per_device_train_batch_size=config.per_device_train_batch_size, per_device_eval_batch_size=config.per_device_eval_batch_size,
            weight_decay=config.weight_decay, logging_steps=config.logging_steps,
            evaluation_strategy=config.evaluation_strategy, eval_steps=config.eval_steps, save_steps=1e6,
            gradient_accumulation_steps=config.gradient_accumulation_steps
        )

        trainer = Trainer(
            model=model_pegasus,
            args=training_args,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_pt['test'],
            eval_dataset=dataset_pt['validation'])

        trainer.train()

        # save model
        model_pegasus.save_pretrained(os.path.join(
            self.config.root_dir, "pegasus-samsum-model"))

        # save tokenizer
        tokenizer.save_pretrained(os.path.join(
            self.config.root_dir, "tokenizer"))
