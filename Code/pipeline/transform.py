import pandas as pd
from typing import List

'''
Function to transform a list of dataframes in a single dataframe
'''

def concat_dfs(dtf_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dtf_list, ignore_index=True)




