import os
import urllib.request as request
import zipfile
from cnnClassifer import logger
from src.cnnClassifer.utils.common import get_size
from cnnClassifer.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None"""

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)