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

    list_of_df = [ele for ele in raw_list_of_df if "Name" == ele.columns[0]][::2]

    df = pd.concat(list_of_df)

    lamb = lambda x: x.split()[-1] + ', ' + x.rsplit(' ', 1)[0]
    df['player_name'] = df['Name'].apply(lamb)
    col = list(df.columns)

    col.insert(0, col.pop())
    df = df[col]

    injury_type = filename.strip('.html').split('_')[1]
    df['injury_type'] = injury_type

    df = df[df['Pos'].notna()]
    df = df[df['Pos'].str.endswith('P', na=False)]

    df = df.drop(['Name'], axis=1)
    cols = list(df.columns)
    col = [cols[0]] + [cols[-1]] + cols[1:-1]
    df = df[col]

    filename_w = filename[:-4] + 'csv'
    to_write = os.path.join(write_directory, filename_w)

    df.to_csv(to_write, index=False)
