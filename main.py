# ****************************** EECE5644 Final Project on Speed Dating ******************************
# ***************** Authors: Robert Ashby, Helena Calatrava, Hwijong Im and Kuo Yang *****************
# Main Function (Created 2022-11-08)
# This function contains the main flow of the code

# Imports
import pandas as pd
import numpy as np

from configuration import Config

if __name__ == '__main__':
    # importing dataset (converted to .xlsx to get around an encoding issue)
    df = pd.read_excel(Config.path_dataset)

    # viewing first 10 rows of dataset
    print(df.head(10))

    # get # rows in dataset
    print(len(df.index))

    # get # of unique participants
    df_no_dupes = df.drop_duplicates(subset=['iid'])
    print(len(df_no_dupes))

    # Average age of participants
    print(int(df_no_dupes.drop_duplicates(subset=['iid'])["age"].mean()))


