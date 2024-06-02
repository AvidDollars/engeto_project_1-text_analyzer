from typing_extensions import Self, Callable, Iterable
from constants import HR_LINE


def normalize_word(*, word: str, chars_to_delete=(" ", ",", ";", ".", "!", "?")) -> str:
    """
    Takes singe word and normalizes it. Normalization is done based on provided characters
    which should be removed from a word. If characters are not provided, the default ones
    will be used for normalization.
    """

    for character in chars_to_delete:
        word = word.replace(character, "")
    return word


class TextLoader:
    """
    Class for loading text for analysis from a data source.
    For each new data source you must implement classmethod that
    returns an instance of the class.
    """

    def __init__(self, *, text) -> None:
        self.data = text

    @classmethod
    def from_plain_file(cls, *, path: str) -> Self:
        """
        Loads a text from plain file and
        returns class instance with a text from loaded file. 
        """

        with open(path, mode="r", encoding="utf-8") as text:
            return cls(text=text.read())


class TokenizedText:
    """
    Normalizes provided text based on provided characters which should be excluded from words.
    """

    def __init__(self, *, text: TextLoader, chars_to_delete: Iterable[str]=(" ", ",", ";", ".", "!", "?")) -> None:
        self.words = [normalize_word(word=word, chars_to_delete=chars_to_delete) for word in text.data.split()]


class TextAnalysis:
    """
    Class for text analysis.
    """

    def __init__(self, *, tokenized_text: TokenizedText) -> None:
        self.text = tokenized_text.words
        self.word_length_counts = {} # SCHEMA: {length: counts}

        for word in self.text:
            counter = self.word_length_counts
            counter[len(word)] = counter.get(len(word), 0) + 1

        self.max_len = max(self.word_length_counts.keys())
        self.max_count = max(self.word_length_counts.values())

    def __repr__(self) -> str:

        # WORD TYPES STATS
        numbers = self.get_all_numbers()
        all_words = f"There are {len(self.all_words)} words in the selected text."
        titlecase_words = f"There are {self.count_filtered_words(filter_=lambda word: word.istitle())} titlecase words."
        uppercase_words = f"There are {self.count_filtered_words(filter_=lambda word: not word[0].isdecimal() and word.isupper())} uppercase words."
        lowercase_words = f"There are {self.count_filtered_words(filter_=lambda word: word.islower())} lowercase words."
        numeric_words = f"There are {len(numbers)} numeric strings."
        sum_of_numbers = f"The sum of all the numbers is {sum(numbers)}."
        
        # LENGTH STATS
        mid_col = "OCCURENCES"
        padding = 2
        max_len = max(self.word_length_counts.keys())
        max_occurences = max(self.word_length_counts.values())
        mid_column_len = max(len(mid_col), max_occurences)
        rows = []

        for length in range(1, max_len + 1):
            count = self.word_length_counts.get(length)

            if count is not None:
                occurences = ("*" * count).ljust(mid_column_len + padding)
                rows.append(f"{str(length).rjust(3)}|{occurences}|{count}")

        # FINAL STRING
        return "\n".join(
            (
                HR_LINE, all_words, titlecase_words, uppercase_words, lowercase_words, numeric_words, sum_of_numbers,
                HR_LINE, f"LEN|{mid_col.center(mid_column_len + padding)}|NR.", HR_LINE, *rows
            )
        )

    @property
    def all_words(self):
        return self.text
    

    def count_filtered_words(self, filter_: Callable[[str], str]) -> int:
        """
        Returns count of words which are filtered based on provied filterer
        """
        return sum(1 for _ in filter(filter_, self.text))
    
    def get_all_numbers(self) -> list[int]:
        """
        Returns list of all words which were converted from "str" to "int"
        """

        numbers = []

        for item in self.text:
            try:
                numbers.append(int(item))
            except ValueError:
                pass

        return numbers
