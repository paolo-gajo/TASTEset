import json
import re

def adjust_annotations(txt_data):
    fraction_mapping = {
        '½': '1/2', '¼': '1/4', '¾': '3/4',
        '⅓': '1/3', '⅔': '2/3', '⅕': '1/5',
        '⅖': '2/5', '⅗': '3/5', '⅘': '4/5',
        '⅙': '1/6', '⅚': '5/6', '⅛': '1/8',
        '⅜': '3/8', '⅝': '5/8', '⅞': '7/8', 
    }
    fraction_pattern = re.compile('|'.join(re.escape(key) for key in fraction_mapping.keys()))

    updated_txt_data = []
    for line in txt_data:
        new_line = ""
        last_index = 0
        for match in re.finditer(fraction_pattern, line):
            start, end = match.span()
            fraction = match.group()
            # Check if fraction is preceded by a number without space
            if start > 0 and line[start-1].isdigit():
                replacement = ' ' + fraction_mapping[fraction]
            else:
                replacement = fraction_mapping[fraction]
            # Add the text before the fraction and the replacement fraction
            new_line += line[last_index:start] + replacement
            last_index = end
        # Add the remaining part of the line
        new_line += line[last_index:]
        # Replace any standalone slash symbols if necessary
        new_line = new_line.replace("⁄", "/")
        updated_txt_data.append(new_line)
    return updated_txt_data

# Example usage
txt_file = '/home/pgajo/working/food/data/TASTEset/data/TASTEset_semicolon_formatted_raw.it'
with open(txt_file, 'r', encoding='utf-8') as file:
    data = file.readlines()

modified_data = adjust_annotations(data)

# save to updated txt file with different name
with open(txt_file[:-3] + '.fixed.it', 'w', encoding='utf-8') as file:
    file.writelines(modified_data)