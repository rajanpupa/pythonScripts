import pandas
filename='machine_learning_pluralsight/dataset/forestfires.csv'
names = ['X', 'Y', 'month', 'day', 'FFMC', 'DMC',
         'DC', 'ISI', 'temp', 'RH', 'wind','rain', 'area']
df= pandas.read_csv(filename,names=names)
print(pandas.isnull(df))
