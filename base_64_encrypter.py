import base64
import optparse

def get_locations() -> (str, str):
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="source_location", help="Target data .txt file")
    parse_object.add_option("-o", "--output", dest="output_location", help="Target data output .txt file")
    options = parse_object.parse_args()[0]
    source_location = options.source_location
    output_location = options.output_location

    return (source_location, output_location)

def get_source_items_to(source_location: str) -> list[str]:
    items = list()  # String list

    with open(source_location, "rb") as f: # We have to get the values as bytes (the 'b' in r represents this) because when we endcode the value, it asks for byte
        for line in f:
            items.append(line)

    return items

def encode_and_add_all_source_items_to_output(target_location: str, items: list[str]):
    with open(target_location, "w") as f:
        for raw_data in items:
            f.write(f"{base64.b64encode(raw_data).decode()}\n")

(source_location, target_location) = get_locations()

try:
    source_items = get_source_items_to("source_location")
    encode_and_add_all_source_items_to_output(target_location, source_items)

    print(f"All words in the target file is encrypted and added to {target_location}")
except Exception as exp:
    print(f"{exp}")