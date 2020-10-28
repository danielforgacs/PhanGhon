"""
Converter for ghost names exported
as CSV file from google sheets to json
to be used as fixture.
"""

import json
import csv

# ADD CSV PATH HERE:
ghostnamesfile = ('....Edit PHANTOM List of Ghost Names - Ghost names.csv')

data = []

with open(ghostnamesfile) as csvfile:
    rowreader = csv.reader(csvfile)
    idx = 0

    for row in rowreader:
        idx += 1
        fields = {
            "model": "phantomname.ghostname",
            "pk": idx,
            "fields": {
                'name': row[0],
                'description': row[1],
            }
        }
        data.append(fields)

print(json.dumps(data, indent=4))
