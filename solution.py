from PIL import Image

word_matrix = Image.open('word_matrix.png')
mask = Image.open('mask.png')

mask = mask.resize(word_matrix.size)
mask.putalpha(128)

word_matrix.paste(mask, (0, 0), mask)
word_matrix.show()
