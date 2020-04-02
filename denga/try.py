from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn

def sentence_similarity(sentence1, sentence2):
    sentence1=pos_tag(word_tokenize(sentence1))
    sentence2=pos_tag(word_tokenize(sentence2))
    print(sentence1)
    print(sentence2)



sentence_similarity("Cats are beautiful animals", "Cats are annoying")
















# from nltk.corpus import wordnet as wn
#
# print(wn.synsets('cat', 'n'))
# print(wn.synsets('dog', 'n'))
# print(wn.synsets('feline', 'n'))
# print(wn.synsets('mammal', 'n'))
#
# cat = wn.synsets('cat', 'n')[0]  # Get the most common synset
# print(cat.lemmas()[0].count())  # Get the first lemma => 18
#
# dog = wn.synsets('dog', 'n')[0]  # Get the most common synset
# feline = wn.synsets('feline', 'n')[0]  # Get the most common synset
# mammal = wn.synsets('mammal', 'n')[0]  # Get the most common synset
#
# for synset in [dog, feline, mammal]:
#     print("Similarity(%s, %s) = %s" % (cat, synset, cat.wup_similarity(synset)))