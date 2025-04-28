from CleanData import data_cleansing
from SummaryStats import summary_stats
from IdentifyAnomalies import anomaly_detection
import os

print("Input base path:")
base_path = input()

print("Action you must to perform:\n1.Clean data and store \n"\
"2.Calculate summary statistics\n 3.Identify anomalies")
action = int(input())

if action == 1:
    print("Data cleansing started")
    data_cleansing(base_path)
    print("Data cleansing completed")
elif action == 2:
    print("Stats calculation started")
    print("Calculate summary for:\n1.Particular date\n2.Entire period")
    summary_action=int(input())
    if summary_action == 1:
        print("Enter date, turbin_id(YYYY-MM-DD,1):")
        input=input()
        date,turbine_id=input.split(",")
        summary_stats(base_path,date,turbine_id)
    else:
        summary_stats(base_path)
    print("Stats calculation completed")
elif action == 3:
    print("Anomaly identification started")
    # Example function call (you would define this function based on your needs)
    anomaly_detection(base_path)
else:
    print("Invalid action selected, Please choose 1, 2, or 3.")