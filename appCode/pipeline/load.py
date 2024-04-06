import pandas as pd
import os 


def load_excel(dtf: pd.DataFrame, output_path: str, file_name:str) -> str:

    '''
    receive a dataframe and save as excel

    arguments:
    dataframe (pd.dDataFrame)= dtf to be saved as excel
    output path (str) = path where to save
    file_name (str) = name of the file to be saved

    return: "File Saved"
    '''

    # If output folder does not exist, create it
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Output to excel
    dtf.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return "File successfuly saved"


