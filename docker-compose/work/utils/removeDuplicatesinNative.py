import json
from collections import OrderedDict

def remove_duplicates(input_file, output_file, unique_id):
    seen_ids = set()
    output_data = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        for item in data:
            id_value = item.get(unique_id)
            if id_value not in seen_ids:
                seen_ids.add(id_value)
                output_data.append(item)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=4)

def remove_duplicates2(input_file, output_file, unique_id):
    unique_objects = OrderedDict()

    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        for item in data:
            id_value = item.get(unique_id)
            if id_value not in unique_objects or len(item) > len(unique_objects[id_value]):
                unique_objects[id_value] = item

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(list(unique_objects.values()), outfile, indent=4)

if __name__ == "__main__":
    input_file = "path/to/your/input.json"
    output_file = "path/to/your/output.json"
    unique_id = "name"

    # Uncomment one of the following lines to use the desired method
    # remove_duplicates(input_file, output_file, unique_id)
    remove_duplicates2(input_file, output_file, unique_id)
