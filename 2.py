def replace_all(text, dct):
    a_dict = {}
    for i, j in dct.items():
        text = text.replace(i, j)
        a_dict['j'] = i
    for x, y in a_dict.items():
        text = text.replace(x, y)
    return text


text = 'AB DMF GR YGI'
c_dict = {'M': 'A', 'Y': 'B', 'D': 'C', 'A': 'M',
          'F': 'T', 'I': 'G', 'R': 'S', 'B': 'Y', 'G': 'I'}
text = replace_all(text, c_dict)
print(text)
