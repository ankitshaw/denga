# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet
#
# lemmatizer = WordNetLemmatizer()
#
# # function to convert nltk tag to wordnet tag
# def nltk_tag_to_wordnet_tag(nltk_tag):
#     if nltk_tag.startswith('J'):
#         return wordnet.ADJ
#     elif nltk_tag.startswith('V'):
#         return wordnet.VERB
#     elif nltk_tag.startswith('N'):
#         return wordnet.NOUN
#     elif nltk_tag.startswith('R'):
#         return wordnet.ADV
#     else:
#         return None
#
# def lemmatize_sentence(sentence):
#     #tokenize the sentence and find the POS tag for each token
#     nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
#     print(nltk_tagged)
#     #tuple of (token, wordnet_tag)
#     wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
#     lemmatized_sentence = []
#     for word, tag in wordnet_tagged:
#         if tag is None:
#             #if there is no available tag, append the token as is
#             lemmatized_sentence.append(word)
#         else:
#             #else use the tag to lemmatize the token
#             lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
#     return " ".join(lemmatized_sentence)
#
# print(lemmatizer.lemmatize("I am loving it")) #I am loving it
# print(lemmatizer.lemmatize("loving")) #loving
# print(lemmatizer.lemmatize("swimming", "v")) #love
# print(lemmatize_sentence("i will be working from home")) #I be love it
#
#
# # # import these modules
# # from nltk.stem import WordNetLemmatizer
# #
# # lemmatizer = WordNetLemmatizer()
# #
# # print("swimming :", lemmatizer.lemmatize("i want to go swimming"))
# # print("corpora :", lemmatizer.lemmatize("corpora"))
# #
# # # a denotes adjective in "pos"
# # print("swim :", lemmatizer.lemmatize("swimming", pos="v"))
#
#
# # import nltk
# # from nltk.corpus import stopwords,wordnet
# # from nltk.tokenize import word_tokenize, sent_tokenize
# # from nltk.tag import DefaultTagger
# # import spacy
# #
# # stop_words = set(stopwords.words('english'))
# # def removeStopWords(sentence):
# #     filtered_sentence = " ".join(filter(lambda word: word not in stop_words, sentence.split()))
# #     return filtered_sentence
# #
# # nlp = spacy.load('en_core_web_lg')
# # a = "i ducked"
# # a1=nlp(removeStopWords(a))
# # print(a1)
# # b = "the duck is yellow"
# # b1=nlp(removeStopWords(b))
# # print(b1)
# # print(nlp(a).similarity(nlp(b)))
# # print(a1.similarity(b1))
# #
#
#
# # # # Program to measure similarity between
# # # # two sentences using cosine similarity.
# # # from nltk.corpus import stopwords
# # # from nltk.tokenize import word_tokenize
# # #
# # # # X = input("Enter first string: ").lower()
# # # # Y = input("Enter second string: ").lower()
# # # X = "I want to swim"
# # # Y = "I wishing to swim"
# # #
# # # # tokenization
# # # X_list = word_tokenize(X)
# # # Y_list = word_tokenize(Y)
# # #
# # # # sw contains the list of stopwords
# # # sw = stopwords.words('english')
# # # l1 = [];
# # # l2 = []
# # #
# # # # remove stop words from string
# # # X_set = {w for w in X_list if not w in sw}
# # # Y_set = {w for w in Y_list if not w in sw}
# # #
# # # # form a set containing keywords of both strings
# # # rvector = X_set.union(Y_set)
# # # for w in rvector:
# # #     if w in X_set:
# # #         l1.append(1)  # create a vector
# # #     else:
# # #         l1.append(0)
# # #     if w in Y_set:
# # #         l2.append(1)
# # #     else:
# # #         l2.append(0)
# # # c = 0
# # #
# # # # cosine formula
# # # for i in range(len(rvector)):
# # #     c += l1[i] * l2[i]
# # # cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
# # # print("similarity: ", cosine)
# #
# # from nltk import word_tokenize, pos_tag
# # from nltk.corpus import wordnet as wn
# #
# #
# # def penn_to_wn(tag):
# #     """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
# #     if tag.startswith('N'):
# #         return 'n'
# #
# #     if tag.startswith('V'):
# #         return 'v'
# #
# #     if tag.startswith('J'):
# #         return 'a'
# #
# #     if tag.startswith('R'):
# #         return 'r'
# #
# #     return None
# #
# #
# # def tagged_to_synset(word, tag):
# #     wn_tag = penn_to_wn(tag)
# #     if wn_tag is None:
# #         return None
# #
# #     try:
# #         return wn.synsets(word, wn_tag)[0]
# #     except:
# #         return None
# #
# #
# # def sentence_similarity(sentence1, sentence2):
# #     """ compute the sentence similarity using Wordnet """
# #     # Tokenize and tag
# #     sentence1 = pos_tag(word_tokenize(sentence1))
# #     sentence2 = pos_tag(word_tokenize(sentence2))
# #
# #     # Get the synsets for the tagged words
# #     synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
# #     synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
# #
# #     # Filter out the Nones
# #     synsets1 = [ss for ss in synsets1 if ss]
# #     synsets2 = [ss for ss in synsets2 if ss]
# #     print(synsets1)
# #     print(synsets2)
# #
# #     score, count = 0.0, 0
# #
# #     # For each word in the first sentence
# #     for synset in synsets1:
# #         # Get the similarity value of the most similar word in the other sentence
# #         best_score = print([synset.path_similarity(ss) for ss in synsets2])
# #
# #         # Check that the similarity could have been computed
# #         if best_score is not None:
# #             score += best_score
# #             count += 1
# #
# #     # Average the values
# #     score /= count
# #     return score
# #
# #
# # sentences = [
# #     "Dogs are awesome.",
# #     "Some gorgeous creatures are felines.",
# #     "Dolphins are swimming mammals.",
# #     "Cats are beautiful animals.",
# # ]
# #
# # focus_sentence = "Cats are beautiful animals."
# #
# # for sentence in sentences:
# #     print(focus_sentence, sentence, sentence_similarity(focus_sentence, sentence))
# #     print(sentence, focus_sentence, sentence_similarity(sentence, focus_sentence))
# #
# #
# #
# #
# #
# #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # from nltk.corpus import wordnet as wn
# # # #
# # # # print(wn.synsets('cat', 'n'))
# # # # print(wn.synsets('dog', 'n'))
# # # # print(wn.synsets('feline', 'n'))
# # # # print(wn.synsets('mammal', 'n'))
# # # #
# # # # cat = wn.synsets('cat', 'n')[0]  # Get the most common synset
# # # # print(cat.lemmas()[0].count())  # Get the first lemma => 18
# # # #
# # # # dog = wn.synsets('dog', 'n')[0]  # Get the most common synset
# # # # feline = wn.synsets('feline', 'n')[0]  # Get the most common synset
# # # # mammal = wn.synsets('mammal', 'n')[0]  # Get the most common synset
# # # #
# # # # for synset in [dog, feline, mammal]:
# # # #     print("Similarity(%s, %s) = %s" % (cat, synset, cat.wup_similarity(synset)))

from ..genda import Genda
import os

gen = Genda(os.path.abspath("denga\\example\\temps.txt"))
gen.generate()
gen.save()

'''
Run this file from main git folder (denga) path as:
    python -m denga.example.try
Output 'denga.txt' will be created in the main git folder (denga)
'''