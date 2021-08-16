def correct_string(str_1, replacements=None):
    if replacements is None:
        replacements = {'M': 'A', 'Y': 'B', 'D': 'C', 'A': 'M',
                        'F': 'T', 'I': 'G', 'R': 'S', 'B': 'Y', 'G': 'I'}
    return ''.join(replacements.get(c, c) for c in str_1)
print(correct_string('AB DMF GR YGI'))

# with open('message.txt') as file:
#     my_file = file.readlines()


