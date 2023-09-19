from textSummarizer.components.model_evaluation import ModelEvaluation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.evaluate()