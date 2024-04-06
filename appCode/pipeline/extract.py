import os # manipulate folders and files
import glob # list files
import pandas as pd # Data frames
from typing import List


def extract_from_excel(path:str) -> List[pd.DataFrame]:
    '''
    Create function to read files from a folder and returna list of dataframes
    
    Arguments: 
    
    * path: input path with the list of files
    
    * return : list of dataframes
    '''

    # List all the files XLSX
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    # Create list of dataframes from excel files
    data_frame_list = []
    for file in all_files:
        dtf = pd.read_excel(file)
        data_frame_list.append(dtf)

    return data_frame_list


if __name__ == "__main__":

    path = "data/input"
    
    data_frame_list = extract_from_excel(path)
    print(data_frame_list) 
