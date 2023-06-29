import pandas as pd

db_1 = pd.read_excel('np_database_1.xlsx')
db_2 = pd.read_excel('np_database_2.xlsx')

db_new = pd.concat([db_1, db_2])

db_new.to_excel('np_database_3.xlsx', index=False)
