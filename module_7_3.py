class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = dict()
        for b in self.file_names:
            s = ''
            with open(b, encoding='utf-8') as file:
                for b in file:
                    s += b.lower()
            s = s.replace(',', ' ').replace('!', ' ').replace('.', ' ').split()
            all_words[b] = s
        return all_words

    def find(self, word):
        words_find = {}
        for name, words in self.get_all_words().items():
            k = 1
            for b in words:
                if b == word.lower():
                    break
                k += 1
        words_find[name] = k
        return words_find

    def count(self, word):
        words_count = {}
        for name, words in self.get_all_words().items():
            k = sum([1 for b in words if b == word.lower()])
            words_count[name] = k
        return words_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
