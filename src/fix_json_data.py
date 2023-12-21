import json
import re

def adjust_annotations(json_data):
    fraction_mapping = {
        '½': '1/2', '¼': '1/4', '¾': '3/4',
        '⅓': '1/3', '⅔': '2/3', '⅕': '1/5',
        '⅖': '2/5', '⅗': '3/5', '⅘': '4/5',
        '⅙': '1/6', '⅚': '5/6', '⅛': '1/8',
        '⅜': '3/8', '⅝': '5/8', '⅞': '7/8',
    }
    fraction_pattern = re.compile('|'.join(re.escape(key) for key in fraction_mapping.keys()))

    for annotation in json_data['annotations']:
        text = annotation['text']
        entities = annotation['entities']
        adjustment = 0

        for match in re.finditer(fraction_pattern, text):
            fraction_index = match.start() + adjustment
            fraction = match.group()
            print(fraction)
            three_char_fraction = fraction_mapping[fraction]
            print(three_char_fraction)
            text = text[:fraction_index] + three_char_fraction + text[fraction_index + 1:]

            # Adjust the indices of subsequent annotations
            for entity in entities:
                start, end = entity[0], entity[1]
                if start == fraction_index:
                    entity[0] = start
                    entity[1] = end + 2
                if start > fraction_index:
                    entity[0] = start + 2
                    entity[1] = end + 2

            adjustment += 2

        annotation['text'] = text

    return json_data

# Example usage
json_file = '/home/pgajo/working/food/data/TASTEset/data/TASTEset.json'
with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

modified_data = adjust_annotations(data)

# save to updated json file with different name
with open(json_file[:-5] + '_updated.json', 'w', encoding='utf-8') as file:
    json.dump(modified_data, file, ensure_ascii=False, indent=4)