import json
import sys
sys.path.append('/home/pgajo/working/food/src/translate')
from tqdm.auto import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
json_path = '/home/pgajo/working/food/data/TASTEset/data/TASTEset.json'

with open(json_path, encoding='utf8') as f:
    data = json.load(f)

raw_lines = []
for line in data['annotations']:
    raw_lines.append(line['text'])

with open(json_path.replace('.json', '.txt'), 'w', encoding='utf8') as f:
    for el in tqdm(raw_lines, total = len(raw_lines)):
        f.write(el+'\n')

model_name = 'Helsinki-NLP/opus-mt-tc-big-en-it'
tokenizer = AutoTokenizer.from_pretrained(model_name)
device = 'cuda'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

model.to(device)

class MarianTranslator:
    def __init__(self, model_name, device):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.model.to(device)
        self.device = device

    def translate(self, text):
        batch = self.tokenizer([text], return_tensors="pt").to(device)
        generated_ids = self.model.generate(**batch, max_new_tokens=1024)
        return self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

translator = MarianTranslator(model_name=model_name, device=device)

raw_lines_translated = [translator.translate(line) for line in tqdm(raw_lines, total = len(raw_lines))]

with open(json_path.replace('.json', '_translated.txt'), 'w', encoding='utf8') as g:
    for el in raw_lines_translated:
        g.write(el+'\n')