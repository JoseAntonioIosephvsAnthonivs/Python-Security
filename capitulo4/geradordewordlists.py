import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string)) #quantidade de dígitos a ser combinados

for i in resultado:
	print(''.join(i))

	zzz = list(enumerate(resultado))
	print(zzz)





















