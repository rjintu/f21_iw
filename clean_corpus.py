# import os 
# import nltk
# from nltk import stem, word_tokenize
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

# in_dir = r'/Users/Firebolt/Documents/Sem5-Fall2021/cos397/f21_iw/data'
# out_dir = r'/Users/Firebolt/Documents/Sem5-Fall2021/cos397/f21_iw/cleaned_data'


# def get_wordnet_pos(word):
#     """Map POS tag to first character lemmatize() accepts"""
#     tag = nltk.pos_tag([word])[0][1][0].upper()
#     tag_dict = {"J": wordnet.ADJ,
#                 "N": wordnet.NOUN,
#                 "V": wordnet.VERB,
#                 "R": wordnet.ADV}

#     return tag_dict.get(tag, wordnet.NOUN)



# lemmatizer = WordNetLemmatizer()

# for filename in os.listdir(in_dir):
#     if filename.endswith('.txt'):
#         print(filename)
#         curr_file = open(os.path.join(in_dir, filename), 'r')
#         line = curr_file.readline()

#         while line:
#             word_list = word_tokenize(line)
#             lemmatized_output = ' '.join([lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in word_list])

#             line = curr_file.readline()


import os
import spacy
import gc
import time
from multiprocessing import cpu_count

start_time = time.time()

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
all_stopwords = nlp.Defaults.stop_words

in_dir = r'/Users/Firebolt/Documents/Sem5-Fall2021/cos397/f21_iw/data'
out_dir = r'/Users/Firebolt/Documents/Sem5-Fall2021/cos397/f21_iw/cleaned_data'

i = 0
n_process = cpu_count() - 1
for filename in os.listdir(in_dir):
    i += 1
    output_list = []
    if filename.endswith('.txt') and filename == 'midwest_opinions_1950-1979.txt':
        num_lines = 0
        print(filename)
        curr_file = open(os.path.join(in_dir, filename), 'r')
        output_file = open(os.path.join(out_dir, os.path.splitext(filename)[0] + '_formatted.txt'), 'w')
        line = curr_file.readline()
        
        input_list = [] # use this to get the input collectively 

        while line:
            input_list.append(line)
            num_lines += 1

            # every 1000 lines, start piping
            if num_lines % 2000 == 0:
                # pipe in batches of 100
                
                for doc in nlp.pipe(input_list, batch_size=50):
                    formatted_line = " ".join([token.lemma_ for token in doc if not token.lemma_ in all_stopwords])
                    # print(formatted_line)
                    output_list.append(formatted_line)

                del input_list
                input_list = []
                gc.collect()

            line = curr_file.readline()

            if num_lines % 10000 == 0:
                print(num_lines)
            
            # periodic bulk write
            if num_lines % 20000 == 0:
                output_file.writelines(output_list)
                print(f'outputted through line {num_lines}')
                del output_list
                output_list = []
                gc.collect()
        
        # remaining lines in input
        if len(input_list) != 0:
            for doc in nlp.pipe(input_list):
                formatted_line = " ".join([token.lemma_ for token in doc if not token.lemma_ in all_stopwords])
                output_list.append(formatted_line)
            del input_list
            input_list = []
            gc.collect()


        # remaining lines
        output_file.writelines(output_list)
        del output_list
        output_list = []
        gc.collect()
        
        curr_file.close()
        output_file.close()
        print(f'{filename} complete!')

end_time = time.time()

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))

time_convert(end_time - start_time)


