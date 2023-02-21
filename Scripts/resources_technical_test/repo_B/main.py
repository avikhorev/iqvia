import logging
import os
import random
import sys
# import yaml
import pandas as pd
# import xlrd
# from datetime import datetime

from src.pipeline import run_pipeline



if __name__ == "__main__":
    # lecture des paramètres du fichier de configuration
    # default_config_file = "config/default.yaml"
    # with open(default_config_file, "r") as f:
    #     default_config = yaml.load(f, Loader=yaml.FullLoader)

    # user_config_file = "config/user_config.yaml"
    # with open(user_config_file, "r") as f:
    #     user_config = yaml.load(f, Loader=yaml.FullLoader)

    if len(sys.argv) < 4:
        print("3 params expected : OUTPUT_FILE_PATH, PARAM1, PARAM2")
        sys.exit(1)
        
    OUTPUT_FILE_PATH = sys.argv[1]
    PARAM1 = sys.argv[2]
    PARAM2 = sys.argv[3]

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('Logger')
    logger.info(f"Script Repo_B running. Params: param1={PARAM1}, param2={PARAM2}")

    # get result from pipeline
    df_results, diag_info = run_pipeline(logger, param1=PARAM1, param2=PARAM2);

    if random.random()>0.5:
        logger.info(f"FAILURE DURING SCRIPT EXECUTION")
        sys.exit(1)
       
    # export results
    with pd.ExcelWriter(OUTPUT_FILE_PATH) as writer:
      df_results.to_excel(writer, index=False)
      sys.exit(0)
