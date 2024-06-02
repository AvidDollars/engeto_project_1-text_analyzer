from utils import TokenizedText, normalize_word, TextLoader, TextAnalysis


text_a = TextLoader(text="[hello] [420] [world] [69]")
text_b = TextLoader(text="One. Two. Three. 1! 2! 3!")

chars_to_delete_a = ("[", "]")
chars_to_delete_b = (".", "!")


def test_finding_all_words_a():
    tokenized_text = TokenizedText(text=text_a.data, chars_to_delete=chars_to_delete_a)
    text_analysis = TextAnalysis(tokenized_text=tokenized_text)

    assert text_analysis.all_words == ["hello", "420", "world", "69"]


def test_finding_all_words_b():
    tokenized_text = TokenizedText(text=text_b.data, chars_to_delete=chars_to_delete_b)
    text_analysis = TextAnalysis(tokenized_text=tokenized_text)

    assert text_analysis.all_words == ["One", "Two", "Three", "1", "2", "3"]


def test_find_all_numbers_a():
    tokenized_text = TokenizedText(text=text_a.data, chars_to_delete=chars_to_delete_a)
    text_analysis = TextAnalysis(tokenized_text=tokenized_text)

    assert text_analysis.get_all_numbers() == [420, 69]


def test_finding_all_numbers_b():
    tokenized_text = TokenizedText(text=text_b.data, chars_to_delete=chars_to_delete_b)
    text_analysis = TextAnalysis(tokenized_text=tokenized_text)

    assert text_analysis.get_all_numbers() == [1, 2, 3]
