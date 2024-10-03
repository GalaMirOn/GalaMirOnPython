class WordsFinder:

    def __init__(self, file_names:list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        spisok_slov = []
        punktuacija = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        names = self.file_names
        # print('Имена файлов = ', names, type(names))
        # for name in names:
        with open(names, encoding = 'utf-8') as file:
            for line in file:
                line = line.lower()
                for simvol in punktuacija:
                    line = line.replace(simvol, '')
                spisok_slov += line.split(' ')
            all_words[names] = spisok_slov
        return all_words

    def find(self, word):
        word = word.lower()
        find_dict = {}
        name = self.file_names
        all_words = self.get_all_words()
        words = all_words[name]
        # print(words.index(word))
        #for name, words in all_words().items():
        find_dict[name] = words.index(word)+1
        return find_dict

    def count(self, word):
        count_dict = {}
        word = word.lower()
        name = self.file_names
        all_words = self.get_all_words()
        words = all_words[name]
        # for name, words in all_words().items():
        count_dict[name] = words.count(word)
        return count_dict


if __name__ == '__main__':

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words()) # Все слова
    print(finder2.find('TEXT')) # 3 слово по счёту
    print(finder2.count('teXT')) # 4 слова teXT в тексте всего