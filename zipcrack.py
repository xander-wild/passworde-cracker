import zipfile
from threading import Thread

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print ('[+] Found password ' + password + '\n')
	except:
		pass
def main():
	zFile = zipfile.ZipFile('evil.zip')
	passFile = open('password.txt')
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()
if __name__ == '__main__':
	main()

	#remaining in programm 
	#create a file file evil.zip 
	#install zipfile module 
	#install thread module 
	