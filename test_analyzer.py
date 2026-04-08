import pytest
from analyzer import TextAnalyzer

@pytest.fixture
def analyzer():
    return TextAnalyzer()

@pytest.fixture
def temp_file(tmp_path):
    def _create_file(content):
        d = tmp_path / "sub"
        d.mkdir()
        f = d / "test.txt"
        f.write_text(content, encoding='utf-8')
        return str(f)
    return _create_file

@pytest.mark.parametrize("text, expected_sentences", [
    ("Hello world.", 1),
    ("Hi! How are you? Fine...", 3),
    ("No sentences here", 0),
    ("Wait... What?! Yes.", 3)
])
def test_count_sentences(analyzer, text, expected_sentences):
    assert analyzer.count_sentences(text) == expected_sentences

@pytest.mark.parametrize("text, expected_words", [
    ("word1, word2: word3; word4", 4),
    ("Simple sentence", 2),
    ("", 0),
    ("Hello,world;test", 3)
])
def test_count_words(analyzer, text, expected_words):
    assert analyzer.count_words(text) == expected_words

def test_read_file(analyzer, temp_file):
    content = "Test content."
    path = temp_file(content)
    assert analyzer.read_file(path) == content