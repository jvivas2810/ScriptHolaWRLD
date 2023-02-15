import sys

ip = sys.argv[1]
mac = sys.argv[2]
ab = sys.argv[3]

ip_log = open("nodos_seguros.dat", "r").read()

#def search_str("nodos_seguros.dat", "{sys.argv[1]}"):
#with open("nodos_seguros.dat", 'r') as file:
#	content = file.read()
#	if "{sys.argv[1]}" in content:
#		variable="hola"



if ab == "A":
	f = open("nodos_seguros.dat","w")
	f.write("\n" f'{sys.argv[1]};{sys.argv[2]}')
elif ab == "B":
	open("nodos_seguros.dat","r")
	f = open("nodos_seguros.dat","w")
	f.write("\n" f'{sys.argv[1]};{sys.argv[2]}')
else:
	"Introduzca A o B"


