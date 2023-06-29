import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

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



"""Объединение"""
db_new = pd.concat([db_1, db_2])

"Исправление артефактов в статистике"
db_new['Nanoparticle'] = np.where(db_new['Nanoparticle'] == 'Iron oxide' , 'IronOxide', db_new['Nanoparticle'])
db_new['Nanoparticle'] = np.where(db_new['Nanoparticle'] == 'IronOide' , 'IronOxide', db_new['Nanoparticle'])
db_new = db_new.drop(db_new[db_new['Cell_Viability (%)'] > 300].index)
db_new['Diameter (nm)'] = np.where(db_new['Diameter (nm)'] == '-', None, db_new['Diameter (nm)'])

"""Построение графиков"""
plt.title('Выживаемость и время инкубации материала с клетками')
sns.scatterplot(data=db_new,
             x = 'Exposure time (h)',
             y = 'Cell_Viability (%)')

plt.title('Выживаемость наночастиц')
sns.scatterplot(data=db_new,
             x = 'Nanoparticle',
             y = 'Cell_Viability (%)')

plt.title('Диаметр к поверхностной модификации')
sns.scatterplot(data=db_new,
             x = 'Coat',
             y = 'Diameter (nm)')

plt.title('Жизнеспособность клеток к поверхностной модификации')
fig, ax = plt.subplots(figsize = (14,8))
ax = sns.scatterplot(data=db_new,
             x = 'Coat',
             y = 'Cell_Viability (%)')
ax.tick_params(axis='x', rotation=45)
plt.show()


"""Сохранение"""
db_new.to_csv('database_new.csv', index=False)
