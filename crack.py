import crypt

def testpass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():

		word = word.strip('\n')
		cryptWord =crypt.crypt(word,salt)

		if (cryptWord ==cryptPass):
			print("[+] Found pasasword :"+word+"\n")
			return

	print("[+] password not found ")
	return

def main():
	passFile = open('password.txt')

	for line in passFile.readlines():

		if ":" in line :
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print("[+] cracking password for :" +user)
			testpass(cryptPass)

if __name__=="__main__":
	main()
	