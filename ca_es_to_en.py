from transformers import MarianMTModel, MarianTokenizer

model_name_es = 'Helsinki-NLP/opus-mt-es-en'
model_name_ca = 'Helsinki-NLP/opus-mt-ca-en'


def setup():
    global tokenizer_es, model_es, tokenizer_ca, model_ca
    tokenizer_es = MarianTokenizer.from_pretrained(model_name_es)
    model_es = MarianMTModel.from_pretrained(model_name_es)
    print(model_name_es + ' loaded')
    tokenizer_ca = MarianTokenizer.from_pretrained(model_name_ca)
    model_ca = MarianMTModel.from_pretrained(model_name_ca)
    print(model_name_ca + ' loaded')


def translate_es(input_text):
    translation = model_es.generate(**tokenizer_es(input_text, return_tensors='pt', padding=True))
    return tokenizer_es.decode(translation[0], skip_special_tokens=True)


def translate_ca(input_text):
    translation = model_ca.generate(**tokenizer_ca(input_text, return_tensors='pt', padding=True))
    return tokenizer_ca.decode(translation[0], skip_special_tokens=True)
