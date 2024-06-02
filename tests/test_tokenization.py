from utils import TokenizedText


text_a = "Hello World! text sample."
text_b = "[INFO]: application has started!"
chars_to_delete_a = ("!", ",", "?", ".")
chars_to_delete_b = ("[", "]", ":", "!")


def test_tokenization_a():
    tokenized_words = TokenizedText(text=text_a, chars_to_delete=chars_to_delete_a)
    expected = ["Hello", "World", "text", "sample"]

    assert tokenized_words.words == expected


def test_tokenization_b():
    tokenized_words = TokenizedText(text=text_a, chars_to_delete=chars_to_delete_b)
    expected = ["Hello", "World", "text", "sample."]

    assert tokenized_words.words == expected


def test_tokenization_c():
    tokenized_words = TokenizedText(text=text_b, chars_to_delete=chars_to_delete_b)
    expected = ["INFO", "application", "has", "started"]
    
    assert tokenized_words.words == expected