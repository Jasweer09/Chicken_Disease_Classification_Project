import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format ='[%(asctime)s]: %(message)s')

projec_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projec_name}/__init__.py",
    f"src/{projec_name}/components/__init__.py",
    f"src/{projec_name}/utils/__init__.py",
    f"src/{projec_name}/config/__init__.py",
    f"src/{projec_name}/config/configuration.py",
    f"src/{projec_name}/pipeline/__init__.py",
    f"src/{projec_name}/entity/__init__.py",
    f"src/{projec_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"

]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file : {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open (file_path, "w") as file_obj:
            pass
        logging.info(f"Creating the empty file:{file_path}")
    else:
        logging.info(f"{file_name} is already exists")