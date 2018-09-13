import pandas as pd

def missing_data(test):
  df_train=test
  total = df_train.isnull().sum().sort_values(ascending=False)
  percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
  missing_data = pd.concat([total, percent], axis=1, keys=['Total_missing', 'Percent_missing'])
  missing_data.head(20)
  return missing_data
