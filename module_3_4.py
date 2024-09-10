def single_root_words(root_word, *other_words):
    other_words_list = list(other_words)
    same_words = []
    flag = False
    for word in other_words:
        if root_word.upper() in word.upper():
            same_words.append(word)
            flag = True

    if not flag:
        for word in other_words:
            if word.upper() in root_word.upper():
                same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'Richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print('Первый тест: ', result1)
print('Второй тест: ', result2)
