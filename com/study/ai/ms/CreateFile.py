import codecs
import random

file = codecs.open('data.txt', 'a+', 'utf-8')
for i in range(100):
    fly = i * 100
    game = i * random.randint(3, 15)
    ice = random.randint(1, 20)
    other = random.randint(6, 25)
    lab = random.randint(1, 33)
    file.write('\n%d %d %d %d %d' % (fly, game, ice, other, lab))
file.close()
