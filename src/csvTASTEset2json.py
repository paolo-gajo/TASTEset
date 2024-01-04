import json
import spacy
import sys
sys.path.append('/home/pgajo/working/food/TASTEset/src')
from tasteset_utils import prepare_data, ENTITIES

def TASTEset2JSON(csv_path):
    recipes, entities = prepare_data(csv_path)
    annotations = [{'text_en': recipe, 'entities_en': ents} for recipe, ents in zip(recipes, entities)]
    training_data = {'classes': ENTITIES, 'annotations': annotations}
    return training_data

def main():
    csv_path = '/home/pgajo/working/food/TASTEset/data/TASTEset_semicolon.csv'
    json_path = csv_path.replace('.csv', '.json')
    training_data = TASTEset2JSON(csv_path)
    with open(json_path, 'w', encoding='utf-8') as outfile:
        json.dump(training_data, outfile, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()