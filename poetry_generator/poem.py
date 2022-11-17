import spacy
# from spacy.pipeline.textcat import Config, single_label_cnn_config
from django.conf import settings
import glob

from tensorflow.keras.callbacks import LambdaCallback
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import get_file
import shutil
import numpy as np
from .neural_network import Neural_Network

# import logging
# logging.getLogger().setLevel(logging.CRITICAL)

# import torch


# from transformers import GPT2Tokenizer, GPT2LMHeadModel

# device = 'cpu'
# if torch.cuda.is_available():
#     device = 'cuda'

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 10000

class Poem:
    def __init__(self) -> None:
        self.word_bank = {}

    def speech_output(self, request):
        if request.method == "POST":
            data=request.POST.get('speech-output')
            return data

    def merge_file(self, infile, outfile, separator=""):
        for line in infile:
            outfile.write(line.strip("\n")+separator)
        outfile.write("\n")
    def merge_text_files(self):
        static_folder = settings.STATICFILES_DIRS[0]
        files = static_folder + '/input/*.txt'
        read_files = glob.glob(files)
        separator = ""
        with open(static_folder + "/merged/result.txt", "wb") as outfile:
            for f in read_files:
                with open(f, 'rb') as infile:
                     shutil.copyfileobj(outfile, infile)



    def bag_of_words(self, tokens):
        for token in tokens:
            if token.text in self.word_bank:
                self.word_bank[token.text] += 1
            else:
                self.word_bank[token.text] = 1

    def tokenize(self):
        # self.merge_text_files()
        # static_folder = settings.STATICFILES_DIRS[0]
        # file = static_folder + '/merged/result.txt'
        # # r = requests.get("https://data.heatonresearch.com/data/t81-558/text/"\
        # #          "treasure_island.txt")
        # # text = r.text
        # with open (file, "r") as f:
        #     text = f.read()
        # print(text[0:1000])
        # print('------')
        # print('printing poem')
        neural = Neural_Network()
        poem = neural.execute_model()
        return poem
        # print(poem)

