### LIBRARIES #################################################################

import os
import subprocess
from os.path import isfile, join

############################################################################

### CREATE #################################################################

def create():
	print("Stworz wlasny rootCA")
	directory = "tls"
	path = os.getcwd()
	path1 = os.path.join(path, directory)
	os.chdir(path1)
	proces = subprocess.call("openssl genrsa -out private/cakey.pem 4096", stdout=subprocess.PIPE ,shell=True, text=True)
	proces = subprocess.call("openssl req -new -x509 -days 3650 -config openssl.cnf -key private/cakey.pem -out certs/cacert.pem", stdout=subprocess.PIPE ,shell=True, text=True)
	proces = subprocess.call("openssl x509 -noout -text -in certs/cacert.pem", stdout=subprocess.PIPE ,shell=True, text=True)
	os.chdir(path)


### OWN CERT #################################################################

def owncert():
	directory = "tls/certs"
	path = os.getcwd()
	path1 = os.path.join(path, directory)
	os.chdir(path1)
	name = input("Podaj nazwe serwera: ")
	name = name + ".pem"
	command = ['openssl genrsa -out', name, '4096']
	command = ' '.join([str(elem) for elem in command])
	proces = subprocess.call(command, stdout=subprocess.PIPE ,shell=True, text=True)
	os.chdir(path)


### KEYS #################################################################

def keys():
	print("Twoje klucze: \n")
	directory = "tls/certs"
	path = os.getcwd()
	path = os.path.join(path, directory)

	onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f)) if f.endswith(('.crt', '.pem'))]
	for file in onlyfiles:
		print(file)


### LOC KEYS #################################################################

def loc_keys():
	print("Lokalizacja kluczy:")
	directory = "tls/certs"
	path = os.getcwd()
	path = os.path.join(path, directory)
	print(path)


### DODAJ #################################################################

def dodaj():
	print("Dodaje plik klucza")
	name = input("Podaj scierzke pliku: ")
	if isfile(name):
		name1 = input("Podaj nazwe pod jaka chcesz wyswietlac klucz: ")
		path1 = os.getcwd() + '/tls/certs/' + name1 + '.crt'
		print(path1)
		if not os.path.isfile(path1):
			command = ['cp', name,  path1]
			command = ' '.join([str(elem) for elem in command])
			proces = subprocess.call(command, stdout=subprocess.PIPE ,shell=True, text=True)
			#print(command)
		else:
			print('Istnieje juz cert o takiej nazwie!')
	else:
		# 'scierzka' XDDD
		print("Nieprawidlowa sciezka pliku")


### CSR #################################################################

def CSR():
	print("Generuje CSR")
	directory = "tls/certs"
	path = os.getcwd()
	path1 = os.path.join(path, directory)
	os.chdir(path1)
	name = input("Podaj nazwe serwera: ")
	name1 = name + ".pem"
	name2 = name + ".csr"
	command = ['openssl req -new -key', name1, '-out', name2]
	command = ' '.join([str(elem) for elem in command])
	proces = subprocess.call(command, stdout=subprocess.PIPE ,shell=True, text=True)
	os.chdir(path)


### REVOKE #################################################################

def revoke():
	print("Revoke podanego klucza")
	path = os.getcwd()
	name = input("Podaj nazwe klucza ktory chcesz revokowac: ")
	name1 = name + ".crt"
	path1 = path + '/tls/' +'openssl.cnf'
	path2 = path + '/tls/certs/' + name1
	path3 = path + '/tls/crl/rootca.crl'
	command = ['openssl ca -config', path1, '-revoke', path2]
	command = ' '.join([str(elem) for elem in command])
	#print(command)
	proces = subprocess.call(command, stdout=subprocess.PIPE ,shell=True, text=True)
	command = ['openssl ca -config', path1, '-gencrl -out', path3]
	command = ' '.join([str(elem) for elem in command])
	proces = subprocess.call(command, stdout=subprocess.PIPE ,shell=True, text=True)
	#print(command)


### REVOKED KEYS #################################################################

def revoked_keys():
	print('revoked_keys')
	path = os.getcwd()
	path1 = path + '/tls/crl/rootca.crl'
	if isfile(path1):
		command = ['openssl crl -in', path1, '-text -noout']
		command = ' '.join([str(elem) for elem in command])
		proces = subprocess.Popen(command, stdout=subprocess.PIPE ,shell=True, text=True)
		wynik, nr = proces.communicate()
		print (wynik)
	else:
		print('Nie ma pliku lub zaden cert nie zostal zrevokowany')


### CHECK KEY #################################################################

def check_key():
	print('check_key')
	path = os.getcwd()
	name = input('Podaj nazwe klucza: ')
	path0 = path + '/tls/certs/cacert.pem'
	path1 = path + '/tls/certs/' + name + '.crt'
	path2 = path + '/tls/crl/rootca.crl'
	path3 = path + '/tls/temp.pem'
	command = ['cat', path0 , path2, '>', path3]
	command = ' '.join([str(elem) for elem in command])
	proces = subprocess.call(command, stdout=subprocess.PIPE ,shell=True, text=True)
	#print(command)
	command = ['openssl verify -extended_crl -verbose -CAfile', path3, '-crl_check', path1]
	command = ' '.join([str(elem) for elem in command])
	proces = subprocess.Popen(command, stdout=subprocess.PIPE ,shell=True, text=True)
	wynik, nr = proces.communicate()
	print (wynik)
	#print(command)


### SIGN #################################################################

def sign():
	print(os.getcwd())
	print("Podpisuje certyfikat(?)")
	directory = "tls/certs"
	path1 = os.getcwd()
	path = os.path.join(path1, directory)

	directory = "tls/openssl.cnf"
	path2 = os.path.join(path1, directory)

	os.chdir(path)
	#print(os.getcwd())
	name = input("Podaj nazwe CSR: ")
	name1 = name + ".csr"
	name2 = name + ".crt"
	command = ['openssl ca -config', path2, '-notext -batch -in', name1, '-out', name2, '-extfile ext_template.cnf']
	command = ' '.join([str(elem) for elem in command])
	proces = subprocess.call(command, stdout=subprocess.PIPE ,shell=True, text=True)
	os.chdir(path1)


### MAIN MENU #################################################################

while(True):

	print('''

	|-----------------------------------------------|
	|						|
	|		Utilities			|
	|						|
	|	create - stworz wlasny rootCA		|
	|						|
	|	owncert - stworz wlasny certyfikat	|
	|						|
	|	keys - show your public keys		|
	|						|
	|	loc_keys - lokalizacja kluczy		|
	|						|
	|	dodaj - dodaj klucz do bazy		|
	|						|
	|	CSR - generuj CSR			|
	|						|
	|	revoke - revoke certyfikatu		|
	|						|
	|	revoked_keys - odwolane klucze		|
	|						|
	|	check_key - sprawdz klucz		|
	|						|
	|	sign - podpisuje CSR			|
	|						|
	|	exit					|
	|_______________________________________________|

	''')
	#operation = ""
	#while(operation == ""):


	operation = input("Co chcesz zrobic?: ")


	if operation == 'create':
		create()

	elif operation == 'owncert':
		owncert()

	elif operation == 'keys':
		keys()

	elif operation == 'loc_keys':
		loc_keys()

	elif operation == 'dodaj':
		dodaj()

	elif operation == 'CSR':
		CSR()

	elif operation == 'revoke':
		revoke()

	elif operation == 'revoked_keys':
		revoked_keys()

	elif operation == 'check_key':
		check_key()

	elif operation == 'sign':
		sign()

	elif operation == 'exit':
		break


#cmd = 'ls -l'
#os.system(cmd)
