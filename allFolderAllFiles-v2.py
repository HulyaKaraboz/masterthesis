# Quellen:
# https://learnpython.com/blog/python-json-to-csv/
# https://docs.python.org/3/library/json.html
# https://docs.python.org/3/library/csv.html#csv.DictWriter
# https://www.educative.io/answers/how-to-remove-items-from-a-dictionary-in-python
# https://stackoverflow.com/questions/48234473/python-attributeerror-dict-object-has-no-attribute-append

import os
import json
import csv
import shutil

#Hier werden die kopierten Daten abgelegt, um vearbeitet zu werden
FILESPACE="C:\FILESPACE"
#Hier liegen die ursprünglichen Roh-Daten
SOURCEFILESPACE="C:\SOURCEFILESPACE"

#Die json-daten aus der Datei laden
def process_json_file(json_file_path, output_csv_file_path):
    try:
        with open(json_file_path) as f:
            json_data = json.load(f)
    except Exception as e:
        print(f"Fehler beim Laden der JSON-Datei {json_file_path}: {e}")
        return

    #Prüfen, ob die Felder vorhanden sind
    if 'boardData' not in json_data or 'id' not in json_data or 'grip' not in json_data:
        print(f"Die JSON-Datei {json_file_path} enthält nicht die erforderlichen Felder.")
        return

    #Datensätze mit isUnusable ignorieren
    if json_data['isUnusable'] == True:
        print('Datensatz ignoriert, weil inUnusable == true')
        return

    #Wert der file-globalen ID aufteilen in vor und nach dem Bindestrich
    splitJsonDataID = json_data['id'].split('-')
    print("trialStep: " + splitJsonDataID[1])
    #wenn der Wert nach Bindestrich >= 3 (3 ist drillOntheWall) ist, dann weitermachen, ansonsten abbrechen
    if int(splitJsonDataID[1]) < 3:
        print('Datensatz ignoriert, weil splitJsonDataID[1] < 3')
        return


    #Die Felder boardData, id und grip extrahieren
    board_data = json_data['boardData']
    #id = json_data['id']
    #Nur den zweiten Wert der id verwenden
    id = splitJsonDataID[1]
    grip = json_data['grip']
    step_timestamp_4 = json_data['stepTimestamp']['4']

    #Datensätze nach timestamp filtern
    #board_data = [entry for entry in board_data if entry['timestamp'] >= step_timestamp_4]

    #Datensätze wo timestamp < steptimestamp4 ist rausfiltern
    filtered_board_data = []
    for entry in board_data:
        if entry['timestamp'] < step_timestamp_4:
            print('Datensatz ignoriert, weil timestamp < stepTimestamp[4]')
        else:
            #entry['timestamp'] -= step_timestamp_4
            filtered_board_data.append(entry)

    #Jeden Eintrag in der Liste von boardData durchgehen
    #Zu jedem Eintrag von boardData die Werte von id und grip hinzufügen
    for entry in filtered_board_data:
        entry['id_no'] = '{}-{}'.format(json_data['id'], grip)
        entry['grip_letter'] = grip
        #Zu jedem Eintrag von orientation, accelerometer und gyroscope die Werte zu x, y und z hinzufügen und aufsplitten
        entry['orientationX'] = entry['orientation'][0]
        entry['orientationY'] = entry['orientation'][1]
        entry['orientationZ'] = entry['orientation'][2]
        entry['accelerometerX'] = entry['accelerometer'][0]
        entry['accelerometerY'] = entry['accelerometer'][1]
        entry['accelerometerZ'] = entry['accelerometer'][2]
        entry['gyroscopeX'] = entry['gyroscope'][0]
        entry['gyroscopeY'] = entry['gyroscope'][1]
        entry['gyroscopeZ'] = entry['gyroscope'][2]
        #Wenn timestamp übernommen wurde mit step_timestamp_4 subtrahieren
        entry['calcTimestamp'] = int(entry['timestamp']) - int(step_timestamp_4)
        #alle Werte über 180 mit 360 sutrahieren damit die plots nur unten graphen haben
        entry['calcOrientationX'] = (float(entry['orientationX']) + int(180)) % 360
        #Einträge löschen
        del entry['orientation']
        del entry['magnetometer']
        del entry['euler']
        del entry['accelerometer']
        del entry['linearaccel']
        del entry['gyroscope']
        del entry['gravity']


    #Wenn keine gültigen Datensätze in der Datei vorhanden sind
    if not filtered_board_data:
        print(f"Keine gültigen Datensätze gefunden in Datei {json_file_path}")
        return


    #Die Header aus der Liste bestimmen
    # headers = board_data[0].keys()

    #Die Header aus der gefilterten Liste bestimmen
    headers = list(filtered_board_data[0].keys())
    print(headers)

    #id_no und grip_letter zum Anfang der Header einfügen
    headers.insert(0, headers.pop(headers.index('grip_letter')))
    headers.insert(0, headers.pop(headers.index('id_no')))

    #Daten in eine CSV-Datei schreiben
    try:
        with open(output_csv_file_path, 'w', newline='\n') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(filtered_board_data)
        print(f"CSV-Datei erfolgreich erstellt: {output_csv_file_path}")
    except Exception as e:
        print(f"Fehler beim Schreiben der CSV-Datei {output_csv_file_path}: {e}")


#CSV-datei erstellen
def convert_json_to_csv_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                json_file_path = os.path.join(root, file)
                output_csv_file_path = os.path.splitext(json_file_path)[0] + '.csv'
                print(f"Verarbeite Datei: {json_file_path}")
                process_json_file(json_file_path, output_csv_file_path)


#Speicherort der Daten für die Weiterverarbeitung vorbereiten. Originaldaten werden nicht gelöscht oder verändert
#neuer Ablageort inkl. Originaldateien
if os.path.exists(FILESPACE+'/data/') and os.path.isdir(FILESPACE+'/data/'):
    shutil.rmtree(FILESPACE+'/data/')
#Quelle der zu kopierenden und dann zu verarbeitenden Daten
shutil.copytree(SOURCEFILESPACE+'/data/', FILESPACE+'/data/')

#Pfad zum Verzeichnis der json-Dateien
#directory_path = 'data'
#convert_json_to_csv_in_directory(directory_path)
convert_json_to_csv_in_directory(os.path.normpath(FILESPACE+'/data/'))

