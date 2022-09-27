from operator import attrgetter
import random
from models.corpus_entry import Entry


class Corpus():
    def __init__(self):
        self.entries: list[Entry] = []


    def add_entry(self, entry: Entry):
        self.entries.append(entry)

    def get_setup_and_punchline(self) -> list[str]:
        satisfied = False

        while not satisfied:
            short = self._get_short()
            long = self._get_long(short)
            if long != -1:
                satisfied = True

        return [short.word, long.word]

    @staticmethod
    def _sort_by(entries:list[Entry], sort_key) -> list[Entry]:
        """
        Returns new list of entries, sorted by given keyword
        Available sort keys:
            -"word"
            -"phonemes"
            -"syllables"

        Args:
            entries (list[Entry]): list of corpus entries
            sort_key (_type_): keyword to sort by

        Returns:
            list[Entry]: new sorted list
        """
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

    def _get_long(self, short:Entry) -> Entry:
        phonemes = short.phonemes
        all_words_sorted_by_phonemes = self._sort_by(self.entries, "phonemes")
        
        first_match = self._find_first_match(phonemes, all_words_sorted_by_phonemes)
        if first_match == -1:
            return -1
        last_match = self._find_last_match(phonemes, all_words_sorted_by_phonemes)
        match_slice = all_words_sorted_by_phonemes[first_match:last_match+1]

        long_matches = self._filter_by_syllables(match_slice, min=short.syllables + 1)
        if len(long_matches) == 0:
            return -1
        
        return random.choice(long_matches)

    def _find_first_match(self, phonemes: list[str], sorted_entries: list[Entry]) -> int:
        arr = sorted_entries
        num_phonemes = len(phonemes)
        low = 0
        high = len(arr) - 1
        res = -1

        while(low <= high):
            mid = (low + high) // 2

            if arr[mid].phonemes[:num_phonemes] > phonemes:
                high = mid - 1
            elif arr[mid].phonemes[:num_phonemes] < phonemes:
                low = mid + 1
            else:
                res = mid
                high = mid -1

        return res

    def _find_last_match(self, phonemes: list[str], sorted_entries: list[Entry]) -> int:
        arr = sorted_entries
        num_phonemes = len(phonemes)
        low = 0
        high = len(arr) - 1
        res = -1

        while (low <= high):
            mid = (low + high) // 2

            if arr[mid].phonemes[:num_phonemes] > phonemes:
                high = mid - 1
            elif arr[mid].phonemes[:num_phonemes] < phonemes:
                low = mid + 1
            else:
                res = mid
                low = mid + 1
        
        return res
