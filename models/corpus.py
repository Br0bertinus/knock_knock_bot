from models.corpus_entry import Entry


class Corpus():
    def __init__(self):
        self.entries = []

    def add_entry(self, entry: Entry):
        self.entries.append(entry)
