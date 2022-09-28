from models.corpus import Corpus
from models.corpus_entry import Entry
from models.joke import Joke
from generators.corpus_builder import CorpusBuilder

corpus_builder = CorpusBuilder()
corpus = corpus_builder.build()

i = 0
while i < 20:
    joke_meat = corpus.get_setup_and_punchline()
    joke = Joke(joke_meat)
    joke.tell()
    i += 1