import os
import pandas as pd

read_directory = 'statcast_raw_csv_files'
write_directory = 'statcast_relevant_predictors_csv_files'


relevant_attributes = ['player_name',
                       'pitcher',
                       'game_date',
                       'game_pk',
                       'at_bat_number',
                       'pitch_number',
                       'pitch_type',
                       'pitch_name',
                       'release_speed',
                       'release_pos_x',
                       'release_pos_z',
                       'zone',
                       'p_throws',
                       'type',
                       'pfx_x',
                       'pfx_z',
                       'plate_x',
                       'plate_z',
                       'vx0',
                       'vy0',
                       'vz0',
                       'ax',
                       'ay',
                       'az',
                       'sz_top',
                       'sz_bot',
                       'effective_speed',
                       'release_spin_rate',
                       'release_extension',
                       'release_pos_y',
                       'spin_axis',
                       ]

file_list = sorted(os.listdir(read_directory))
for file in file_list:
    filename = os.fsdecode(file)

    to_read = os.path.join(read_directory, filename)

    df_to_read = pd.read_csv(to_read)

    df = df_to_read[relevant_attributes]

    df = df.reindex(index=df.index[::-1])

    pd.set_option('display.max_columns', None)

    df['pitch_of_game'] = df.groupby('game_pk').cumcount() + 1

    col = list(df.columns)

    col.insert(4, col.pop())
    df = df[col]

    year = filename[:4]
    filename_w = f"{year}_statcast_relevant.csv"
    to_write = os.path.join(write_directory, filename_w)

    df.to_csv(to_write, index=False)


