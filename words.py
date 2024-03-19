#deleted orignial list
def print_upper_words(words):
    for word in words:
        if word.startswith(('e', 'E')):
            print(word.upper())
print_upper_words(['everybody', 'hurts', 'sometimes'])
print_upper_words(['everybody', 'Eats', 'eggs', 'each', 'and', 'Every', ''])