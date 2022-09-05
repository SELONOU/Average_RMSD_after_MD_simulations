import pandas as pd
import os
names = [ ]
average = []

files_directory = "csv_files"
for file_name in (os.listdir(files_directory)):
    df=pd.read_csv("%s/%s" %(files_directory, file_name), header=None)

    av = df[1].mean()
    print(file_name, av)
    names.append(file_name)
    average.append(av)
df_results=pd.DataFrame()
df_results["Names"]=names
df_results["average_values"]=average
df_results.to_csv("all_results_average.csv")
