# tokenize json

import json
from nltk.tokenize import word_tokenize, WhitespaceTokenizer

json_path = '/home/pgajo/working/food/data/TASTEset/data/TASTEset.json'

with open(json_path, encoding='utf8') as f:
    data = json.load(f)

for i, recipe in enumerate(data['annotations'][:10]):
    print(i, '---------------------')
    text = recipe['text']
    print('original text:', text)
    print()
    print('tokenized merged text:', ' '.join(word_tokenize(text)))
    print()
    for entity in recipe['entities']:
        print(text[entity[0]:entity[1]])

    