import nltk
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import DefaultTagger
import spacy

stop_words = set(stopwords.words('english'))
def removeStopWords(sentence):
    filtered_sentence = " ".join(filter(lambda word: word not in stop_words, sentence.split()))
    return filtered_sentence

nlp = spacy.load('en_core_web_lg')
a = "i want to swim"
a1=nlp(removeStopWords(a))
print(a1)
b = "i neediness to swim"
b1=nlp(removeStopWords(b))
print(b1)
print(nlp(a).similarity(nlp(b)))



# # # Program to measure similarity between
# # # two sentences using cosine similarity.
# # from nltk.corpus import stopwords
# # from nltk.tokenize import word_tokenize
# #
# # # X = input("Enter first string: ").lower()
# # # Y = input("Enter second string: ").lower()
# # X = "I want to swim"
# # Y = "I wishing to swim"
# #
# # # tokenization
# # X_list = word_tokenize(X)
# # Y_list = word_tokenize(Y)
# #
# # # sw contains the list of stopwords
# # sw = stopwords.words('english')
# # l1 = [];
# # l2 = []
# #
# # # remove stop words from string
# # X_set = {w for w in X_list if not w in sw}
# # Y_set = {w for w in Y_list if not w in sw}
# #
# # # form a set containing keywords of both strings
# # rvector = X_set.union(Y_set)
# # for w in rvector:
# #     if w in X_set:
# #         l1.append(1)  # create a vector
# #     else:
# #         l1.append(0)
# #     if w in Y_set:
# #         l2.append(1)
# #     else:
# #         l2.append(0)
# # c = 0
# #
# # # cosine formula
# # for i in range(len(rvector)):
# #     c += l1[i] * l2[i]
# # cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
# # print("similarity: ", cosine)
#
# from nltk import word_tokenize, pos_tag
# from nltk.corpus import wordnet as wn
#
#
# def penn_to_wn(tag):
#     """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
#     if tag.startswith('N'):
#         return 'n'
#
#     if tag.startswith('V'):
#         return 'v'
#
#     if tag.startswith('J'):
#         return 'a'
#
#     if tag.startswith('R'):
#         return 'r'
#
#     return None
#
#
# def tagged_to_synset(word, tag):
#     wn_tag = penn_to_wn(tag)
#     if wn_tag is None:
#         return None
#
#     try:
#         return wn.synsets(word, wn_tag)[0]
#     except:
#         return None
#
#
# def sentence_similarity(sentence1, sentence2):
#     """ compute the sentence similarity using Wordnet """
#     # Tokenize and tag
#     sentence1 = pos_tag(word_tokenize(sentence1))
#     sentence2 = pos_tag(word_tokenize(sentence2))
#
#     # Get the synsets for the tagged words
#     synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
#     synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
#
#     # Filter out the Nones
#     synsets1 = [ss for ss in synsets1 if ss]
#     synsets2 = [ss for ss in synsets2 if ss]
#     print(synsets1)
#     print(synsets2)
#
#     score, count = 0.0, 0
#
#     # For each word in the first sentence
#     for synset in synsets1:
#         # Get the similarity value of the most similar word in the other sentence
#         best_score = print([synset.path_similarity(ss) for ss in synsets2])
#
#         # Check that the similarity could have been computed
#         if best_score is not None:
#             score += best_score
#             count += 1
#
#     # Average the values
#     score /= count
#     return score
#
#
# sentences = [
#     "Dogs are awesome.",
#     "Some gorgeous creatures are felines.",
#     "Dolphins are swimming mammals.",
#     "Cats are beautiful animals.",
# ]
#
# focus_sentence = "Cats are beautiful animals."
#
# for sentence in sentences:
#     print(focus_sentence, sentence, sentence_similarity(focus_sentence, sentence))
#     print(sentence, focus_sentence, sentence_similarity(sentence, focus_sentence))
#
#
#
#
#
#
# #
# #
# #
# #
# #
# #
# # # from nltk.corpus import wordnet as wn
# # #
# # # print(wn.synsets('cat', 'n'))
# # # print(wn.synsets('dog', 'n'))
# # # print(wn.synsets('feline', 'n'))
# # # print(wn.synsets('mammal', 'n'))
# # #
# # # cat = wn.synsets('cat', 'n')[0]  # Get the most common synset
# # # print(cat.lemmas()[0].count())  # Get the first lemma => 18
# # #
# # # dog = wn.synsets('dog', 'n')[0]  # Get the most common synset
# # # feline = wn.synsets('feline', 'n')[0]  # Get the most common synset
# # # mammal = wn.synsets('mammal', 'n')[0]  # Get the most common synset
# # #
# # # for synset in [dog, feline, mammal]:
# # #     print("Similarity(%s, %s) = %s" % (cat, synset, cat.wup_similarity(synset)))