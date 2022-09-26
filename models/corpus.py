from operator import attrgetter
import random
from models.corpus_entry import Entry


class Corpus():
    def __init__(self):
        self.entries: list[Entry] = []


    def add_entry(self, entry: Entry):
        self.entries.append(entry)

    @staticmethod
    def _sort_by(entries:list[Entry], sort_key):
        sorted_entries = sorted(entries, key=attrgetter(sort_key))
        return sorted_entries


    @staticmethod
    def _filter_by_syllables(entries: list[Entry], min = 1, max = 99) -> list[Entry]:
        filtered = [entry for entry in entries if min <= entry.syllables <= max]
        return filtered


    def _get_short(self) -> Entry:
        short_words = self._filter_by_syllables(self.entries, min=1, max=2)
        random_entry = random.choice(short_words)
        return random_entry


    
