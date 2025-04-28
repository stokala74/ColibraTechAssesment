import pandas as pd
import numpy as numpy
import os
from datetime import datetime

def anomaly_detection(base_path):
    file_path=os.path.join(base_path,'Output','stats')
    for file in os.listdir(file_path):
        if file.endswith('.csv'):
            file_path=os.path.join(file_path,file)
            df=pd.read_csv(file_path)

            mean_output=np.mean(df['avg_power_op'])
            std_dev=np.std(df['avg_power_op'])

            lower_bound=mean_output - 2*std_dev
            upper_bound=mean_output + 2*std_dev
            current_date=datetime.now().strftime('%Y-%m-%d')

            anomalies_df=df[(df['avg_power_op']<lower_bound)|(df['avg_power_op']>upper_bound)]
            anomalies_df.to_csv(os.path.join(base_path,'Output','anomalies',f'anomalies_{current_date}.csv'))
            print(f"Anomalies saved to anomalies_{current_date}.csv")