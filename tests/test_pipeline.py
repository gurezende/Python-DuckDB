import pandas as pd
from Code.pipeline.transform import concat_dfs

df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
df_2 = pd.DataFrame({'col1': [5,6], 'col2': [7,8]})

def test_concat_dataframes():

    # Arrange
    df_list = [df_1, df_2]

    # Act
    df = concat_dfs(df_list)

    # assert
    assert df.shape == (4,2)
