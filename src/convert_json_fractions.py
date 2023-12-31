import json
import re

# Regular expression pattern for matching Unicode fraction characters and forms like "1⁄2"
fraction_pattern = re.compile(
    r'[\u00BC-\u00BE\u2150-\u215E]|(\d+)\u2044(\d+)'  # This pattern now includes the vulgar fraction form
)

# A dictionary mapping Unicode fractions to their plain text equivalents
fraction_mapping = {
    '½': '1/2', '⅓': '1/3', '⅔': '2/3', '¼': '1/4', '¾': '3/4',
    '⅕': '1/5', '⅖': '2/5', '⅗': '3/5', '⅘': '4/5', '⅙': '1/6',
    '⅚': '5/6', '⅐': '1/7', '⅛': '1/8', '⅜': '3/8', '⅝': '5/8',
    '⅞': '7/8', '⅑': '1/9', '⅒': '1/10', '⅟': '1',
    # The following line adds support for common vulgar fractions
    '1\u20442': '1/2', '1\u20443': '1/3', '2\u20443': '2/3', '1\u20444': '1/4', '3\u20444': '3/4',
    # Add any other specific fractions like this as needed
}

def convert_fractions(text):
    """
    Replaces all Unicode fraction characters and "number⁄number" forms with their plain text equivalents.
    """
    def replacement(match):
        # This function will be used to return the right fraction replacement
        if match.group(1):  # This is the case for "number⁄number" forms
            return match.group(1) + '/' + match.group(2)
        else:  # This is the case for single Unicode fraction characters
            return fraction_mapping.get(match.group(), '')

    # Substitute fractions with their plain text equivalents using the replacement function
    return fraction_pattern.sub(replacement, text)

def process_json_file(file_path):
    """
    Load a JSON file, replace all fractions in string values, and save the results.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Assume that the JSON object is a dictionary
    for key, value in data.items():
        if isinstance(value, str):
            data[key] = convert_fractions(value)
        # If the value is a list or another dictionary, additional handling is required

    # Convert the modified data back to JSON
    json_data = json.dumps(data, ensure_ascii=False, indent=2)

    # Write the modified JSON data back to a new file
    with open(file_path.replace('.json', '_slash.json'), 'w', encoding='utf-8') as file:
        file.write(json_data)
    print(f"Processed JSON saved to 'modified_{file_path}'")

def process_text_file(file_path):
    """
    Load a text file, replace all fractions, and save the results to a new file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Convert the fractions to plain text
    modified_content = convert_fractions(content)

    # Write the modified content back to a new file
    with open(file_path[:-4] + '_slash' + file_path[-4:], 'w', encoding='utf-8') as file:
        file.write(modified_content)
    print(f"Processed file saved to 'modified_{file_path}'")

# Replace 'your_file.json' with your JSON file path
process_text_file('/home/pgajo/working/food/TASTEset/data/TASTEset_semicolon.csv')
