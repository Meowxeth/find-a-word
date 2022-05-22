def paragraph_to_list(filepath):
    with open(filepath, 'r') as f_obj:
        lines = f_obj.readlines()

    special_characters = ['.', ' ', '', ',', '!', '?', '-', '(', ')', '\n']
    words_in_the_paragraph = []
    word = []

    for line in lines:
        for letter in line:
            if letter not in special_characters:
                word.append(letter)
            elif letter in special_characters:
                words_in_the_paragraph.append("".join(word))
                word.clear()

    return words_in_the_paragraph


def find_word(listed_pargraph=[], word_to_find=''):
    ammount_of_times_appeared = sum(
        word_to_find.lower() == word for word in listed_pargraph)

    print(f'The word \'{word_to_find}\' appeared '
          f'{ammount_of_times_appeared} times.')


find_word(paragraph_to_list('paragraph.txt'), 'The')
