from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger
import os


STAGE_NAME = "Evaluation stage"

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/AkashKulkarni4444/KidneyDiseaseClassification.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="AkashKulkarni4444"
os.environ["MLFLOW_TRACKING_PASSWORD"]="a5822a71ae059c7a235dcb34190305eb72d1b62e"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            