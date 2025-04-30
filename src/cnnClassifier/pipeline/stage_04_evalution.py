from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evalution import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Evalution stage"

class EvalutionPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evalution = Evaluation(val_config)
        evalution.evaluation()
        evalution.save_score()

if __name__ == '__main__':
    try:
        logger.info(f"***************************************************")
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started<<<<<<<")
        obj = EvalutionPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==============x")
    except Exception as e:
        logger.exception(e)
        raise e
