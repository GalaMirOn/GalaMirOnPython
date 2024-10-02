def custom_write(file_name, strings: list):
    file = open(file_name, 'w', encoding='utf-8')
    result = dict()
    for i in range(len(strings)):
        # print(i + 1, '', file.tell(), '', strings[i])
        keys = ((i + 1, file.tell()))
        values = strings[i]
        result[keys] = values
        file.write(strings[i] + '\n')
    file.close()
    return result

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
