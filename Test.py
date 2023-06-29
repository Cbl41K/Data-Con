import pandas as pd
import numpy as np

"""Чтение баз"""
db_1 = pd.read_excel('database1.xlsx')
db_2 = pd.read_excel('database2.xlsx')

"""Изменение значений в столбце Surface_Charge"""
db_1['Surface_Charge'] = np.where(db_1['Surface_Charge'] > 0, 'Positive',
                       np.where(db_1['Surface_Charge'] < 0, 'Negative',
                        np.where(db_1['Surface_Charge'] == 0, 'Neutral', 'Unknown')))

"""Исправление отрицательной выживаемости"""
db_1['Cell_Viability (%)'] = np.where(db_1['Cell_Viability (%)'] < 0, 0, db_1['Cell_Viability (%)'])
db_2['Cell_Viability (%)'] = np.where(db_2['Cell_Viability (%)'] < 0, 0, db_2['Cell_Viability (%)'])

"""Объединение и сохранение"""
db_new = pd.concat([db_1, db_2])
db_new.to_csv('database_new.csv', index=False)
