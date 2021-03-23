s = r"""
Slowly the hippos sank into the river
The water so cold that it gave them a shiver
(Hippos can't swim, like the pelicans think
They also can't float, they could easily sink)"""

# clean up
# s = s.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '')
# or
s = s.lower().translate(str.maketrans('','',',.!?(){}[]'))
# or
# import re
# s = re.sub(r'[^a-zA-Z0-9 ]', '', s)

words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    n = words.count(word)
    d[word] = n

for word, n in sorted(d.items()):
    print('%-25s: %3d' % (word, n))
    # print(f'{word:<25}: {n:3}')
    # or
    # print('%-15s: %3d %s' % (word, n, '*'*n))
