import os

def create():
	print("Tworzy klucze")

def key():
	print("Twoj klucz publiczny")

def loc_keys():
	print("Lokalizacja kluczy")

def dodaj():
	print("Dodaje plik z kluczem publicznym")

def CSR():
	print("Generuje CSR")

def revoke():
	print("Revoke podanego klucza")

def podpisz():
	print("Podpisuje certyfikat(?)")



while(True):

	print('''

	|-----------------------------------------------|
	|						|
	|			Utilities		|
	|						|
	|	create - stworz wlasna pare kluczy	|
	|						|
	|	key - show your public key		|
	|						|
	|	loc_keys - lokalizacja kluczy		|
	|						|
	|	dodaj - dodaj klucz do bazy		|
	|						|
	|	CSR - generuj CSR			|
	|						|
	|	revoke - revoke certyfikatu		|
	|						|
	|	podpisz - podpisuje plik(?)		|
	|						|
	|	exit					|
	|_______________________________________________|

	''')
	#operation = ""
	#while(operation == ""):
	operation = input()

	if operation == 'create':
		create();
	elif operation == 'key':
		public_key();
	elif operation == 'loc_keys':
		loc_keys();
	elif operation == 'dodaj':
		dodaj();
	elif operation == 'CSR':
		CSR();
	elif operation == 'revoke':
		revoke();
	elif operation == 'podpisz':
		podpisz();
	elif operation == 'exit':
		break;




#cmd = 'ls -l'
#os.system(cmd)
