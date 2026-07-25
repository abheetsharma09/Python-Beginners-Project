import csv
import json
import os

file_path_input = input("Enter JSON file Path.. ")

if os.path.exists(file_path_input):
    if os.path.getsize(file_path_input) == 0:
        print(f"Error: '{file_path_input}' is completely empty.")
        json_data = []
    else:
        try:
            with open(file_path_input, "r", encoding="utf-8") as file:
                json_data = json.load(file)
        except json.JSONDecodeError:
            print(f"Error: '{file_path_input}' contains invalid JSON.")
            json_data = []

    if json_data:
        if not isinstance(json_data, list):
            json_data = [json_data]

        csv_file_path = "./CSV/finalDATA.csv"
        file_exists = os.path.exists(csv_file_path)

        existing_names = set()
        start_sl_no = 1

        if file_exists:
            with open(csv_file_path, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                headers_in_file = next(reader, None)

                if headers_in_file:
                    try:
                        name_idx = headers_in_file.index("product_name")
                    except ValueError:
                        name_idx = None

                    valid_rows = 0
                    for row in reader:
                        if row and any(cell.strip() for cell in row):
                            valid_rows += 1
                            if name_idx is not None and len(row) > name_idx:
                                existing_names.add(row[name_idx].strip())

                    start_sl_no = valid_rows + 1

        items_to_append = []
        for item in json_data:
            name = item.get("product_name", "").strip()
            if name not in existing_names:
                items_to_append.append(item)

        if items_to_append:
            with open(
                csv_file_path, mode="a", newline="", encoding="utf-8"
            ) as file:
                writer = csv.writer(file)

                if not file_exists or start_sl_no == 1:
                    headers = ["Sl No"] + list(items_to_append[0].keys())
                    writer.writerow(headers)

                for index, item in enumerate(items_to_append, start=start_sl_no):
                    row = [index] + list(item.values())
                    writer.writerow(row)

            print(
                f"Successfully appended {len(items_to_append)} new unique item(s)."
            )
        else:
            print("No new data to add. All items already exist in the CSV.")
else:
    print("File doesn't found!!")
