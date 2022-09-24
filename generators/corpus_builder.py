import nltk
import cmudict
import syllables

from models.corpus import Corpus
from models.corpus_entry import Entry


class CorpusBuilder():
    def __init__(self):
        self.cmu_words = cmudict.entries()


    def build(self):
        corpus = Corpus()
        for cmu_word in self.cmu_words:
            word = cmu_word[0]
            phonemes = cmu_word[1]
            corpus.add_entry(self._new_entry(word, phonemes))
        return corpus

    def _new_entry(self, word, phonemes):
        entry = Entry()
        entry.word = word
        entry.phonemes = phonemes
        entry.syllables = syllables.estimate(word)
        return entry
