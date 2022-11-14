import spacy
from spacy.pipeline.textcat import Config, single_label_cnn_config
from django.conf import settings
import glob
import logging
logging.getLogger().setLevel(logging.CRITICAL)

import torch
import numpy as np

from transformers import GPT2Tokenizer, GPT2LMHeadModel

device = 'cpu'
if torch.cuda.is_available():
    device = 'cuda'

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 1600000
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-xl')
model = GPT2LMHeadModel.from_pretrained('gpt2-xl')
model = model.to(device)
class Poem:
    def __init__(self) -> None:
        self.word_bank = {}

    def speech_output(self, request):
        if request.method == "POST":
            data=request.POST.get('speech-output')
            # print('printing data')
            print(data)
            return data

    def merge_text_files(self):
        static_folder = settings.STATICFILES_DIRS[0]
        files = static_folder + '/input/*.txt'
        read_files = glob.glob(files)
        with open(static_folder + "/merged/result.txt", "wb") as outfile:
            for f in read_files:
                with open(f, 'rb') as infile:
                    outfile.write(infile.read())

    def tokenize(self):
        self.merge_text_files()
        static_folder = settings.STATICFILES_DIRS[0]
        file = static_folder + '/merged/result.txt'
        with open (file, "r") as f:
            text = f.read()

        tokens = nlp(text)
        tokens = [token for token in tokens if not token.is_stop and not token.is_punct]

        for token in tokens:
            if token.text in self.word_bank:
                print('f')
                self.word_bank[token.text] += 1
            else:
                self.word_bank[token.text] = 1
        print(self.word_bank)
    
        # self.generate_some_text("Asian Americans are amazing", 100)

    
    def choose_from_top(self, probs, n=5):
        ind = np.argpartition(probs, -n)[-n:]
        top_prob = probs[ind]
        top_prob = top_prob / np.sum(top_prob) # Normalize
        choice = np.random.choice(n, 1, p = top_prob)
        token_id = ind[choice][0]
        return int(token_id)

    def generate_some_text(self,input_str, text_len = 500):
        cur_ids = torch.tensor(tokenizer.encode(input_str)).unsqueeze(0).long().to(device)
        model.eval()
        with torch.no_grad():
            for i in range(text_len):
                outputs = model(cur_ids, labels=cur_ids)
                loss, logits = outputs[:2]
                softmax_logits = torch.softmax(logits[0,-1], dim=0) #Take the first(only one) batch and the last predicted embedding
                next_token_id = self.choose_from_top(softmax_logits.to('cpu').numpy(), n=10) #Randomly(from the given probability distribution) choose the next word from the top n words
                cur_ids = torch.cat([cur_ids, torch.ones((1,1)).long().to(device) * next_token_id], dim = 1) # Add the last word

            output_list = list(cur_ids.squeeze().to('cpu').numpy())
            output_text = tokenizer.decode(output_list)
            print(output_text)
 
        # config = Config().from_str(single_label_cnn_config)



        # if "textcat" not in nlp.pipe_names:
        #     nlp.add_pipe('textcat', config=config, last=True)
        # textcat = nlp.get_pipe('textcat')
        # textcat.add_label("uplifting")
        # print(nlp.pipe_names)

     

    