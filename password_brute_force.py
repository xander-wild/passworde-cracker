import random
import pyautogui

char="0123456789abcdefghijklmnopqrstuvwxyz"
charlist=list(char)


password=pyautogui.password("enter password here:")

guess_password=''
while (guess_password !=password):
	guess_password=random.choices(charlist,k=len(password))

	print("<>>>"+str(guess_password)+"<<<>")

	if (guess_password==list(password)):
		print("your password is :"+"".join(guess_password))
		break
