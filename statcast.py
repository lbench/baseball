from pybaseball import statcast, cache, statcast_pitcher, playerid_lookup
import pandas as pd

cache.enable()

stat_2020 = statcast(start_dt="2020-01-01", end_dt="2020-12-31")
stat_2020.to_csv("2020_statcast.csv")

stat_2021 = statcast(start_dt="2021-01-01", end_dt="2021-12-31")
stat_2021.to_csv("2021_statcast.csv")

stat_2022 = statcast(start_dt="2022-01-01", end_dt="2022-12-31")
stat_2022.to_csv("2022_statcast.csv")

stat_2023 = statcast(start_dt="2023-01-01", end_dt="2023-12-31")
stat_2023.to_csv("2023_statcast.csv")

stat_2024 = statcast(start_dt="2024-01-01", end_dt="2024-04-23")
stat_2024.to_csv("2024_statcast.csv")

