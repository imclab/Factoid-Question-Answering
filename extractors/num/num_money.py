# -*- coding: utf-8 -*-
'''
100 feet
9 inches
fifty miles
seven yards
3.2 feet
.99 meters
half a meter
'''
from __future__ import division
import sys
sys.path.append('/home/gavin/dev/Factoid-Question-Answering')
from collections import defaultdict
from interfaces import ner_interface


def extract(tokens, pos_tagged_documents, ranked_docs):
    ner = ner_interface.NER_interface()
    answer_freq = defaultdict(int)

    for doc in ranked_docs:
        for entities in ner.get_money_entities(doc):
            for entity in entities:
                answer_freq[entity] += 1

    print len(answer_freq)
    for i in answer_freq.items():
        print i
    if len(answer_freq) == 0:
        answers = ["Sorry, I couldn't find any answers for that."]
    else:
        answers = sorted(
            answer_freq.items(), key=lambda x: x[1], reverse=True)[0]
    return 'factoid', answers[0], answers, None


#def extract(tokens, pos_tagged_documents, ranked_docs):
    #'''

    #'''
    #currencies_file = os.path.join(os.path.dirname(__file__),
        #'../../resources/gazetteer_currency.txt')
    #with open(currencies_file) as f:
        #currency_surface_forms = f.read().splitlines()

    #numerals_regex = re.compile(r'^[0-9]+\.[0-9]+$')
    #fraction_regex = re.compile(r'[0-9]+/[0-9]+')
    #letters_regex = re.compile(r'[a-zA-Z ]+')
    #int_regex = re.compile(r'[0-9]+')
    #answer_freq = defaultdict(int)

    #for doc in pos_tagged_documents:
        #for index, (token, tag) in enumerate(doc):
            #if tag == 'CD':
                #if doc[index + 1][0] in currency_surface_forms:
                    #print token, doc[index + 1][0]
                    #answer_freq[token] += 1
                #elif doc[index - 1][0] in currency_surface_forms:
                    #print doc[index - 1][0], token
                    #answer_freq[token] += 1

    #best_answer = sorted(
        #answer_freq.items(), key=lambda x: x[1], reverse=True)[0][0]
    #if str(best_answer).endswith('.0'):
        #best_answer = int(best_answer)
    #return best_answer


#def convert_to_numeral(textnum, numwords={}):
    #units = [
    #"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    #"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    #"sixteen", "seventeen", "eighteen", "nineteen",
    #]
    #tens = ["", "", "twenty", "thirty", "forty",
              #"fifty", "sixty", "seventy", "eighty", "ninety"]
    #scales = ["hundred", "thousand", "million", "billion", "trillion"]

    #numwords["and"] = (1, 0)
    #for idx, word in enumerate(units):
        #numwords[word] = (1, idx)
    #for idx, word in enumerate(tens):
        #numwords[word] = (1, idx * 10)
    #for idx, word in enumerate(scales):
        #numwords[word] = (10 ** (idx * 3 or 2), 0)

    #current = result = 0
    #for word in textnum.split():
        #if word not in numwords:
            #raise Exception("Illegal word: " + word)

        #scale, increment = numwords[word]
        #current = current * scale + increment
        #if scale > 100:
            #result += current
            #current = 0

    #return result + current