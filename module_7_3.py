class WordsFinder:

    def __init__(self, *file_names: list):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        punktuacija = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        names = [*self.file_names]
        # print('Имена файлов = ', names, type(names))
        for name in names:
            spisok_slov = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for simvol in punktuacija:
                        line = line.replace(simvol, '')
                    spisok_slov += line.split(' ')
                all_words[name] = spisok_slov
        return all_words

    def find(self, word):
        word = word.lower()
        find_dict = {}
        names = [*self.file_names]
        all_words = self.get_all_words()
        for name in names:
            words = all_words[name]
            find_dict[name] = words.index(word) + 1
        return find_dict

    def count(self, word):
        count_dict = {}
        word = word.lower()
        names = [*self.file_names]
        all_words = self.get_all_words()
        for name in names:
            words = all_words[name]
            count_dict[name] = words.count(word)
        return count_dict


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt', 'test.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))
