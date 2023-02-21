import time
import random
import numpy as np
import pandas as pd

def run_pipeline(logger, **kwargs):
    '''
    This function returns one pandas dataframe with the results, and debug info
    '''

    # This is just dummy code designed to return gibberish, but deterministic output
    input_hash = hash(str(kwargs))
    random.seed(input_hash)
    logger.info("Sleeping...")
    time.sleep(20 + 2 * (input_hash % 10) / 10.)
    logger.info("Done sleeping...")

    output_df = pd.DataFrame(data=np.random.random(size=(1000, 3)), columns=["metric_1", "metric_2", "result"])
    debug_info = {"result": "OK"}

    return output_df, debug_info
