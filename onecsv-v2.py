import pandas as pd
import os
import glob

#Hier liegen die vearbeiteten Daten
FILESPACE="C:\FILESPACE"

#Startverzeichnis
#start_directory = "data"
start_directory = os.path.normpath(FILESPACE+'/data/')

#Liste aller CSV-Dateien in allen Unterverzeichnissen erstellen
all_filenames = []
for root, dirs, files in os.walk(start_directory):
    for file in files:
        if file.endswith('.csv'):
            all_filenames.append(os.path.join(root, file))

#Überprüfen, ob Dateien gefunden wurden
if not all_filenames:
    print("Keine CSV-Dateien gefunden.")
else:
    #Alle Dateien in der Liste kombinieren
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames], ignore_index=True)

    #Exportieren zur CSV-Datei
    output_csv_file_path = os.path.join(start_directory, "combined_csv.csv")
    combined_csv.to_csv(output_csv_file_path, index=False, encoding='utf-8-sig')
    print(f"Kombinierte CSV-Datei erfolgreich erstellt: {output_csv_file_path}")

