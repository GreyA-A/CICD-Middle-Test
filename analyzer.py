import re

class TextAnalyzer:
    def read_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    def count_sentences(self, text):
        # Речення закінчуються на: ..., ., !, ?
        sentences = re.findall(r'\.{3}|[.!?]', text)
        return len(sentences)