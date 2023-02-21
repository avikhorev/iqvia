import sys
import time
import os
import random
from datetime import datetime
import numpy as np
import pandas as pd
# import yaml
import logging


def run(**kwargs):
    """
    Main
    """
    # This is just dummy code designed to return gibberish
    input_hash = hash(str(kwargs))
    random.seed(input_hash)
    np.random.seed(input_hash % 1000)
    logger.info("Computing...")
    time.sleep(1 + 4 * (input_hash % 10) / 10.)
    logger.info("Done computing.")

    logger.info("We have %d positives (mean confidence %.2f%%)" % (int(np.random.normal(500, 100)), np.random.beta(80, 20)))
    output_df = pd.DataFrame(data=np.random.random(size=(100, 10)), columns=["metric_%d" % i for i in range(1, 10)] + ["result"])
    debug_info = {"result": "OK"}

    return output_df, debug_info


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('Logger')
    # yaml_file = "configs/default.yaml"

    # with open(yaml_file, "r") as f:
    #     default_config = yaml.load(f, Loader=yaml.FullLoader)
        
    # yaml_file_user = "configs/user.yaml"
    # with open(yaml_file_user, "r") as f:
    #     user_config = yaml.load(f, Loader=yaml.FullLoader)

    if len(sys.argv) < 3:
        print("2 params expected : OUTPUT_FILE_PATH and PARAM1")
        sys.exit(1)
        
    OUTPUT_FILE_PATH = sys.argv[1]
    PARAM1 = sys.argv[2]
    logger.info(f"Script Repo_A running. Params: param1={PARAM1}")

    # df_results, diag_info = run(default_config=default_config, user_config=user_config)
    df_results, diag_info = run(dummy_arg='random str 123', par=PARAM1)


    # export results
    with pd.ExcelWriter( OUTPUT_FILE_PATH ) as writer:
       df_results.to_excel(writer, index=False)
       sys.exit(0)
