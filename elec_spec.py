import sys
name=sys.argv[1]

arq = file(name,'r').readlines()

for i in range(len(arq)):
#	print arq[i].split()
	if len(arq[i].split()) > 1:
		if arq[i].split()[0] == 'ORBITAL' and arq[i].split()[1] == 'ENERGIES' : break


arqout = file('orbitais.dat', 'w')
arqout.write('#st   #eV    #lb\n')

Homo=479
Lumo=Homo + 1
EWin = 15
linOrbs=i+4
Ofirst = Homo - EWin
Olast =  Lumo + EWin
for i in range(linOrbs+Ofirst,linOrbs+Olast+1):
	Oid = int(arq[i].split()[0])
	if Oid <= Homo:
		arqout.write(str(Oid) + '  '+'{:7.4f}'.format(float(arq[i].split()[3])) + ' H-'+'{:d}'.format(Homo-Oid)+'\n')
	else:
		arqout.write(str(Oid) + '  '+'{:7.4f}'.format(float(arq[i].split()[3])) + ' L+'+'{:d}'.format(Oid-Lumo)+'\n')

arqout.close()
