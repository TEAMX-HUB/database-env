import csv
from pathlib import Path
import json

def csv_to_json(csv_filepath, json_filepath):
    json_array = []
      
    with open(csv_filepath, encoding='utf-8') as csvf: 
        csv_reader = csv.DictReader(csvf) 

        for row in csv_reader: 
            json_array.append(row)
  
    with open(json_filepath, 'w', encoding='utf-8') as jsonf: 
        json_string = json.dumps(json_array, indent=4)
        jsonf.write(json_string)
          
csvFilePath = Path.cwd() / 'assets/class_schedule.csv'
jsonFilePath = Path.cwd() / 'assets/class_schedule.json'

csv_to_json(csvFilePath, jsonFilePath)