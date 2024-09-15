import pandas as pd
import os

#Hier liegen die vearbeiteten Daten
FILESPACE="C:\FILESPACE"
os.path.normpath(FILESPACE+'/data/')

#csv datei lesen
#df = pd.read_csv("data/combined_csv.csv")
df = pd.read_csv(os.path.normpath(FILESPACE+'/data/combined_csv.csv'))

#grip in jeden datensatz überprüfen und gruppiert als csv-datei abspeichern
for grip in ['U', 'P', 'D']:
    grip_df = df[df["grip_letter"] == grip]
    #print(grip_df)
    print(os.path.normpath(FILESPACE+'/data/'+grip.lower()+"_grip.csv"))
    output_csv_path = os.path.normpath(FILESPACE+'/data/'+grip.lower()+"_grip.csv")
    grip_df.to_csv(output_csv_path, index=False)
    print(f"CSV-Datei erfolgreich erstellt: {output_csv_path}")


