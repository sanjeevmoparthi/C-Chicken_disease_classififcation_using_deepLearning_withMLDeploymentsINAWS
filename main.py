from cnnClassifer import logger
from cnnClassifer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifer.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifer.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifer.pipeline.stage_04_evaluation import EvaluationPipeline



STAGE_NAME = "Data Ingestion stage"


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======x")

    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Prepare base model"
try:
    logger.info(f"*****************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model= PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Training"
try:
    logger.info(f"*****************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model=ModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Evaluation stAGE"
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

