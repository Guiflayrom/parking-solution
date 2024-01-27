from WST import WST
from time import sleep as s
from pyscreenshot import grab

input()
s(3)

control = WST()
def get_name():
	import random
	letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	nome = ''
	for i in range(0,16):
		l = letras[random.randint(0,len(letras)-1)]
		nome += l
	return nome + '.jpg'

def change_tab(): control.remotary(["#hkeyctrl tab"])        

def get_print(): 
    filepath = "img/"
    for tab in range(5):
        filename = get_name()
        s(2)
        img = grab()
        img.save(filepath+str(tab)+filename, 'jpeg')              
        change_tab()


times = 479
while times < 480:
    get_print()
    times += 1
    s(1)
