from models.corpus import Corpus
from models.corpus_entry import Entry
from generators.corpus_builder import CorpusBuilder

corpus_builder = CorpusBuilder()
corpus = corpus_builder.build()

print("Done")