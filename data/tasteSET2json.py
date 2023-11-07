import pandas as pd
import re
import json

df = pd.read_csv('/home/pgajo/working/food/TASTEset/data/TASTEset_semicolon.csv')
print(df.head())

# extract each row as an element and put them all in a list
data = df.values.tolist()
print(data[0])
data[0][0] = data[0][0].split(';')
print('data[0]', data[0])
print('data[0][0]', data[0][0])
print('data[0][1]', data[0][1])

data_new = []
recipe_dict = {}
for i, recipe in enumerate(data):
    recipe_dict[i] = {}
    recipe_ingredients_list = recipe[0] # ['5 ounces rum', '4 ounces triple sec', '3 ounces Tia Maria', '20 ounces orange juice']
    # recipe_entities_list = re.findall(r'\{[^{}]*\}', recipe_entities_str)
    recipe_entities_list = re.findall(r'\{.*?"type": ".*?".*?"type": "FOOD".*?\}', recipe[1]) # [{"start": 0, "end": 1, "type": "QUANTITY", "entity": "5"},{"start": 2, "end": 8, "type": "UNIT", "entity": "ounces"},{"start": 9, "end": 12, "type": "FOOD", "entity": "rum"},{"start": 13, "end": 14, "type": "QUANTITY", "entity": "4"},{"start": 15, "end": 21, "type": "UNIT", "entity": "ounces"},{"start": 22, "end": 32, "type": "FOOD", "entity": "triple sec"},{"start": 33, "end": 34, "type": "QUANTITY", "entity": "3"},{"start": 35, "end": 41, "type": "UNIT", "entity": "ounces"},{"start": 42, "end": 51, "type": "FOOD", "entity": "Tia Maria"},{"start": 52, "end": 54, "type": "QUANTITY", "entity": "20"},{"start": 55, "end": 61, "type": "UNIT", "entity": "ounces"},{"start": 62, "end": 74, "type": "FOOD", "entity": "orange juice"}]
    for j, ingredient in enumerate(recipe_ingredients_list):
        print(j, recipe_entities_list[j])
    print('------------------------------------')
#         ingredient_dict = json.load(recipe_entities_list[j])
#         recipe_dict[i][j] = {
#             'ingredients': recipe_ingredients_list,
#         }

        

#         ingredient_tuple = (ingredient, recipe_entities_list[i])

# data_dict
# 1
#     'ingredients':{
#         '5 ounces rum': {"start": 0, "end": 1, "type": "QUANTITY", "entity": "5"}
#         '4 ounces triple sec': {"start": 2, "end": 8, "type": "UNIT", "entity": "ounces"}
#         '3 ounces Tia Maria': {

#         }
#         '20 ounces orange juice': {

#         }
#     }
