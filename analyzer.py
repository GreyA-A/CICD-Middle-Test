import re

class TextAnalyzer:
    def read_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()