import re

class TextAnalyzer:
    def read_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    def count_sentences(self, text):
        # Речення закінчуються на: ..., ., !, ?
        sentences = re.findall(r'\.{3}|[.!?]+', text)
        return len(sentences)
    def count_words(self, text):
        # Розділювачі: пробіл, кома, двокрапка, крапка з комою
        words = re.split(r'[ ,:;\n]+', text)
        # Видаляємо порожні елементи (наприклад, якщо було два пробіли)
        words = [w for w in words if w.strip()]
        return len(words)