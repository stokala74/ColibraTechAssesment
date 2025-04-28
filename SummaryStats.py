import pandas as pd
import os
from datetime import datetime

def summary_stats(base_path,date=None,turbine_id=None):
    clean_path=os.path.join(base_path,'Output','cleaned')
    files = os.listdir(cleanpath)
    combined_df=pd.DataFrame()
    for file in files:
        if file.endswith('.csv'):
            file_path=os.path.join(clean_path,file)
            #print(file_path)
            df = pd.read_csv(file_path)
            df['timestamp']=pd.to_datetime(df['timestamp'])

            summ_df = df.groupby([df['timestamp'].dt.date,'turbine_id']).agg(
                min_power_op=('power_output','min'),
                max_power_op=('power_output','max'),
                avg_power_op=('power_output',lambda x: round(x,mean(),2)),
                std_dev_op=('power_output',lambda x: round(x,std(),2)),
            )
            combined_df=pd.concat([combined_df.summ_df])

    current_date=datetime.now().strftime('%Y-%m-%d')
    summary_file=os.path.join(base_path,'Output','stats',f'turbine_stats_{current_date}.csv')
    combined_df.to_csv(summary_file)
    print(f"Stats saved to {summary_file}")
    if date and turbine_id:
        filtered_df=combined_df[(combined_df.index.get_level_values(0) == pd.to_datetime(date).date()) & combined_df.index.get_level_values(1) == int(turbine_id)]
        print(filtered_df)
