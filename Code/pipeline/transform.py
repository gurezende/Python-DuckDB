import pandas as pd
from typing import List



def concat_dfs(dtf_list: List[pd.DataFrame]) -> pd.DataFrame:

    '''
    Function to transform a list of dataframes in a single dataframe
    '''

    return pd.concat(dtf_list, ignore_index=True)




