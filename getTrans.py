import sys
name=sys.argv[1]
Nstates = int(sys.argv[2])

arq = file(name,'r').readlines()

for i in range(len(arq)):
#	print arq[i].split()
	if len(arq[i].split()) > 0:
		if arq[i].split()[0] == 'CIS-EXCITED': break

lincis=i+5

for i in range(lincis,len(arq)):
#	print arq[i].split()
	if len(arq[i].split()) > 0:
		if arq[i].split()[0] == 'ABSORPTION': break

lintab=i+5

outname = name+'_'+ str(Nstates) +'_trans.txt'
arqout = file(outname,'w')

for i in range(lintab,lintab+Nstates):
	arqout.write( arq[i].split()[2] +'  '+ arq[i].split()[3]+'\n')

	if float(arq[i].split()[2]) > 400 and float(arq[i].split()[2]) < 600:
		print arq[i].split()[0],arq[i].split()[2]
arqout.close()




