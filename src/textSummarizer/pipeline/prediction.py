from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
        
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained("/content/tokenizer")
        gen_kwargs = {"length_penalty":0.8, "num_beams":8, "max_length":128}

        sample_text = text

        pipe = pipeline("summarization", model="pegasus-samsum-model", tokenizer=tokenizer)
        summary = pipe(sample_text, **gen_kwargs)

        return summary[0]['summary_text']