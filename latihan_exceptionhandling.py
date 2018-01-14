try:
	f=open("myfile,txt","r")
except FileNotFoundError:
	print("File tidak ada")