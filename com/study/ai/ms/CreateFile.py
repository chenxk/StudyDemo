import codecs
import random

file = codecs.open('data.txt', 'a+', 'utf-8')
for i in range(100):
    fly = i * 100
    game = i * random.randint(3, 5)
    ice = random.randint(1, 10)
    other = random.randint(6, 25)
    lab = random.randint(1, 3)
    file.write('\n%d %d %d %d %d' % (fly, game, ice, other, lab))
file.close()
