import os
import pandas as pd

read_directory = 'fangraphs_htmls'
write_directory = 'fangraphs_csv_files'

file_list = sorted(os.listdir(read_directory))

REMOVE_UNDISCLOSED = True
if REMOVE_UNDISCLOSED:
    file_list = [name for name in file_list if 'undisclosed' not in name]

for file in file_list:
    filename = os.fsdecode(file)

    to_read = os.path.join(read_directory, filename)

    raw_list_of_df = pd.read_html(to_read)

    list_of_df = [ele for ele in raw_list_of_df if "Name" == ele.columns[0]]
