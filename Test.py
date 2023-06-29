import pandas as pd
import numpy as np

"""Чтение баз"""
db_1 = pd.read_excel('database1.xlsx')
db_2 = pd.read_excel('database2.xlsx')

"""Удаление лишнего"""
db_1 = db_1.drop(columns = ['Unnamed: 2', '№'])
db_2 = db_2.drop(columns = ['Unnamed: 0', 'No', 'Unnamed: 4' ] )

"""Изменение значений в столбце Surface_Charge"""
db_1['Surface_Charge'] = np.where(db_1['Surface_Charge'] > 0, 'Positive',
                       np.where(db_1['Surface_Charge'] < 0, 'Negative',
                        np.where(db_1['Surface_Charge'] == 0, 'Neutral', 'Unknown')))
db_2['Surface_Charge'] = np.where(db_2['Surface_Charge'] == 'unknown', 'Unknown', db_2['Surface_Charge'])

"""Изменение значений в столбце Cell age: embryonic (E), Adult (A)"""
db_2['Cell age: embryonic (E), Adult (A)'] = np.where(db_2['Cell age: embryonic (E), Adult (A)'] == 'Adult', 'A',
                       np.where(db_2['Cell age: embryonic (E), Adult (A)'] == 'Embryonic', 'E',
                        np.where(db_2['Cell age: embryonic (E), Adult (A)'] == 'Fetus', 'E', 'Unknown')))

"""Исправление отрицательной выживаемости"""
db_1 = db_1.drop(db_1[db_1['Cell_Viability (%)'] < 0].index)
db_2 = db_2.drop(db_2[db_2['Cell_Viability (%)'] < 0].index)

"""Объединение и сохранение"""
db_new = pd.concat([db_1, db_2])
db_new.to_csv('database_new.csv', index=False)
