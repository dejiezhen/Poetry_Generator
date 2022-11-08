import os
from select import select
from poem import Poem
import spacy

nlp = spacy.load('en_core_web_sm')
f = open('the_city_in_the_sea.txt', 'r')
doc = nlp(f.read())
for token in doc:
    print(token.text, token.pos_, token.dep_)

def select_language():
    get_language = input("Which language do you want to generate a new poem out of? (English/Spanish/Chinese) ")
    available_languages = ['chinese', 'spanish', 'english']
    while get_language.lower() not in available_languages:
        get_language = input("Which language do you want to generate a new poem out of? (English/Spanish/Chinese) ")
    return get_language


def main():
    # grab from inspiring set - chinese, english, spanish (read inputs)
    # selected_language = select_language()
    # if selected_language == 'chinese':
    # elif selected_language == 'spanish':
    
    # default english
    # new_poems = Poem()
    # new_poems.generate_poems()
    
    # if spanish/chinese. get the translated version for inspiring set


    pass

if __name__ == "__main__":
    main()