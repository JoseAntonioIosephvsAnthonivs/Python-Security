import random, string

tamanho = 16

chars = string.ascii_letters + string.digits + '!@#$%&*()-+'

rnd = random.SystemRandom()

print('Senha aleatória gerada: ')
print('-' * 16)
print(''.join(rnd.choice(chars) for i in range(tamanho)))
print('-' * 16)