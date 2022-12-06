# import re
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer
# sia = SentimentIntensityAnalyzer()
# stopwords = nltk.corpus.stopwords.words("english")
# def remove_content(text):
#     text = re.sub(r"http\S+", "", text) #remove urls
#     text=re.sub(r'\S+\.com\S+','',text) #remove urls
#     text=re.sub(r'\@\w+','',text) #remove mentions
#     text =re.sub(r'\#\w+','',text) #remove hashtags
#     return text
# def process_text(text, stem=False): #clean text
#     text=remove_content(text)
#     text = re.sub('[^A-Za-z]', ' ', text.lower()) #remove non-alphabets
#     tokenized_text = nltk.word_tokenize(text) #tokenize
#     clean_text = [
#          word for word in tokenized_text
#          if word not in stopwords
#     ]
#     if stem:
#         clean_text=[stemmer.stem(word) for word in clean_text]
#     return ' '.join(clean_text)

from transformers import AutoTokenizer, AutoModelForSequenceClassification
# Download pytorch model

def text_analysis(text_to_analysis):

    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    inputs = []
    for text in text_to_analysis:
        inputs.append(tokenizer(text,return_tensors="pt"))
    inputs =tokenizer()

    # Transform input tokens

from transformers import (
    pipeline,
    GPT2LMHeadModel,
    GPT2Tokenizer
)

class NLP:
    def __init__(self):
        self.gen_model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.gen_tokenizer = GPT2Tokenizer.from_pretrained('gpt2') 

    def sentiments(self, text: list):
        nlp = pipeline("sentiment-analysis")
        pos =0
        neg = 0;
        for i in text:
            if "NEGATIVE" in nlp(i)[0]['label']:
                neg+=1
            else:
                pos+=1

        result = nlp(i)[0]['label']
        return f"positive: {pos}, negative: {neg}"