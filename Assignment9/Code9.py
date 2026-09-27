import csv
import json

input_file = "input.csv"
output_file = "output.json"

with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print("CSV data successfully converted to JSON.")
print("Data written to", output_file)