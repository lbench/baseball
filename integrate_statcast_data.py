import os
import pandas as pd


read_directory = 'statcast_relevant_predictors_csv_files'
write_file = 'statcast_data.csv'

file_list = sorted(os.listdir(read_directory))

first = True
for file in file_list:
    filename = os.fsdecode(file)

    to_read = os.path.join(read_directory, filename)

    if first:
        df = pd.read_csv(to_read)
        first = False

    else:
        new_df = pd.read_csv(to_read)

        df = pd.concat([df, new_df])



df.to_csv(write_file, index=False)