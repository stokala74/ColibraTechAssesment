import pandas as pd
import os
from pathlib import Path

def remove_outliers(df,column_name,lower_bound,upper_bound):
    df=df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]
    return df

def data_cleansing(base_path):
    source_path = os.path.join(base_path,'Input')
    destination_path = os.path.join(base_path,'Output','cleaned')
    files = os.listdir(source_path)
    #print(source_path)
    for file in files:
        #print(file)
        if file.endswith('.csv'):
            file_path=Path(source_path)/file
            df = pd.read_csv(file_path)
            df = df.dropna()
            #print(df.head(10))
            outlier_cols = ['wind_speed','power_output']
            for col in outlier_cols:
                if col in df.columns:
                    lower_bound = df[col].quantile(0.01)
                    upper_bound = df[col].quantile(0.99)
                    df = remove_outliers(df,col,lower_bound,upper_bound)
            file=file.removesuffix(".csv")
            target_file=os.path.join(destination_path,file+'cleaned.csv')
            #print(target_file)
            df.to_csv(target_file)
            print(f"Cleaned data written to {target_file}")