#synonym sets

import nltk

nltk.download('wordnet')

from nltk.corpus import wordnet as wn

poses = { 'n':'noun', 'v':'verb', 's':'adj (s)', 'a':'adj', 'r':'adv'}
for synset in wn.synsets("good"):
 print("{}: {}".format(poses[synset.pos()],
 ", ".join([l.name() for l in synset.lemmas()])))

print('------------------------------')
panda = wn.synset("panda.n.01")
hyper = lambda s: s.hypernyms()
for h in list(panda.closure(hyper)):
 print(h)