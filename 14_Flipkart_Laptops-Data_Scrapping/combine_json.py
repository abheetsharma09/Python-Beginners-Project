import glob
import json
import os

# Define the folder path and output file
folder_path = "./JSON"
output_file = "combined_list.json"

combined_data = []

# Find all JSON files in the directory
json_files = glob.glob(os.path.join(folder_path, "*.json"))

for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as infile:
        try:
            data = json.load(infile)
            if isinstance(data, list):
                combined_data.extend(data)  # Flatten lists together
            else:
                combined_data.append(data)  # Append single objects
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON file: {file_path}")

# Save the combined data
with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(combined_data, outfile, indent=4)
