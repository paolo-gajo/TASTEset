from nltk.tokenize import word_tokenize, WhitespaceTokenizer
from tqdm.auto import tqdm
src_recipes = '/home/pgajo/working/food/data/TASTEset/data/TASTEset_raw.txt'

with open(src_recipes, 'r', encoding='utf8') as f:
    src_data = f.readlines()

# sample_sentence = data_json['annotations'][0]['text']

# print('sample_sentence', sample_sentence)

# tokenized_sent = word_tokenize(sample_sentence)
# sent_spans = WhitespaceTokenizer().span_tokenize(sample_sentence)

# print('tokenized_sent', tokenized_sent)
# print('sent_spans', [el for el in sent_spans])

tokenized_list = [word_tokenize(line) for line in tqdm(src_data, total =  len(src_data))]

with open(src_recipes.replace('.txt', '_tokenized.txt'), 'w', encoding='utf8') as f:
    for line in tokenized_list:
        f.write(' '.join(line)+'\n')