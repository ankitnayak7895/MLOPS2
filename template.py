# this is a template file and in this file I have to keep what all the 
# files I want to create in my project in automated way not manual way with
# complete paths.

import os
from pathlib import Path
import logging

# print(Path("a\b\c.txt"))


# So,we have to create the list of files

list_of_files=[
      
      ".github/workflows/.gitkeep", # used for CI/CDeployment 
      
      "src/__init__.py", # this is the source code folder
      
      "src/components/__init__",
      "src/components/data_ingestion.py",
      "src/components/data_information.py",
      "src/components/model_trainer.py",
      "src/components/model_evalution.py",
      
      "src/pipeline/__init__.py",
      
      "src/pipeline/training_pipeine.py",
      "src/pipeline/prediction_pipeline.py",
      
      "src/utils/__init__.py",
      "src/utils/utils.py",
      
      "src/logger/__init__.py",
      "src/logger/logger.py",
      
      "src/exception/__init__.py",
      "src/exception/exceptions.py"
      
      "test/unit/__init__.py",
      "test/integration/__init__.py",
      
      "init_setup.sh",
      
      "requirements.txt",
      
      "requirements_dev.txt",
      
      "setup.py",
      
      "setup.cfg",
      
      "pyproject.toml",
      
      "tox.ini",
      
      "experiments/experiment.ipynb"
]

# .gitkeep file means if i want to push the particular folder which is empty
# to the github then I can create a file with name .gitkeep that will
# help to push but it is not visible in the github.

for filepath in list_of_files:
      filepath=Path(filepath)
      filedir,filename=os.path.split(filepath)
      
      if filedir !="":
            os.makedirs(filedir,exist_ok=True)
            logging.info(f"Creating directory:{filedir} for the file {filename}")
            
      if not(os.path.exists(filepath) and os.path.getsize(filepath)==0):
            with open(filepath,'w') as f:
                  pass # create an empty file
                  logging.info(f"Creating empty file:{filepath}")