import ctranslate2
import pyonmttok
from huggingface_hub import snapshot_download
from transformers import MarianMTModel, MarianTokenizer

model_name_es = 'Helsinki-NLP/opus-mt-es-en'
# model_name_ca = 'Helsinki-NLP/opus-mt-ca-en'
model_name_ca = 'softcatala/opennmt-cat-eng'

def setup():
    global tokenizer_es, model_es, tokenizer_ca, model_ca
    tokenizer_es = MarianTokenizer.from_pretrained(model_name_es)
    model_es = MarianMTModel.from_pretrained(model_name_es)
    print(model_name_es + ' loaded')

    # tokenizer_ca = MarianTokenizer.from_pretrained(model_name_ca)
    # model_ca = MarianMTModel.from_pretrained(model_name_ca)
    model_ca_dir = snapshot_download(repo_id=model_name_ca, revision='main')
    tokenizer_ca = pyonmttok.Tokenizer(mode='none', sp_model_path=model_ca_dir + '/sp_m.model')
    model_ca = ctranslate2.Translator(model_ca_dir)
    print(model_name_ca + ' loaded')


def translate_es(input_text):
    translation = model_es.generate(**tokenizer_es(input_text, return_tensors='pt', padding=True))
    return tokenizer_es.decode(translation[0], skip_special_tokens=True)


def translate_ca(input_text):
    # translation = model_ca.generate(**tokenizer_ca(input_text, return_tensors='pt', padding=True))
    # return tokenizer_ca.decode(translation[0], skip_special_tokens=True)
    tokenized = tokenizer_ca.tokenize(input_text)
    translation = model_ca.translate_batch([tokenized[0]])
    return tokenizer_ca.detokenize(translation[0][0]['tokens'])