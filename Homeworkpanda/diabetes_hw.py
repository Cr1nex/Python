import numpy as np
import pandas as pd

def print_first_ten(db):
   print(db.head(10))

# Print the information about the data types, columns, null value counts, memory consumption
def print_modded(db):
   data_types = db.dtypes
   columns = db.columns
   null_values = db.isnull().sum()
   memory_usage = db.info()
   
   summary_data = {
   "Column Name": columns,
   "Data Type": data_types,
   "Null Count": null_values,
    }
   summary_df = pd.DataFrame(summary_data)
   summary_df


# Print basic statistical details about the data
def print_stats(db):  
   db_dc =  db.describe()
   print(db_dc)
   db_dc_t= db_dc.T
   print(db_dc_t)

def replace_zero():
   db = pd.read_csv("diabetes.csv")
   cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
   db[cols] = db[cols].replace(0, np.nan)
   return db

def replace_nan(db):
   mean = db.mean(skipna = True)
   db.fillna(mean,inplace = True)





if __name__ == '__main__':
   pd.options.display.max_rows = 9999
   db = replace_zero()
   replace_nan(db)
   print_first_ten(db)
   print_modded(db)
   print_stats(db)
   
 