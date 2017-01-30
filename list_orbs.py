def fix(string,sgn):
	i = 0
	fixed=''
	while string[i] != sgn:
		fixed=fixed+string[i]
		i+=1
	return fixed

import sys


arq = file('TransLabels.in','r').readlines()

selectedTransWL = []
selectedTrans   = []
for trans in arq:
#	print trans.split()[0],trans.split()[1]
	selectedTrans.append(trans.split()[0])
	selectedTransWL.append(trans.split()[1])
		
Norbs= len(selectedTrans)

dotout = sys.argv[1]

arq = file(dotout, 'r').readlines()



for i in range(len(arq)):
#	print arq[i].split()
	if len(arq[i].split()) > 0:
		if arq[i].split()[0] == 'CIS-EXCITED': break

#print arq[i]
lintab=i+5
#print arq[lintab]

ALLtrans =[]
i = lintab
orbcount = 0
while orbcount < Norbs:
	flagfound = 0
	label=fix(arq[i].split()[1],':')

	if label in selectedTrans:
#		print 'transition:',label, 'ok'
		orbcount+=1
		flagfound=1		

	i+=1
	csum=0
	trans = []
	while len(arq[i].split()) !=0:
		if flagfound == 1:
#			print arq[i].split()[0],arq[i].split()[1],arq[i].split()[2],'  ' ,arq[i].split()[4]
			trans.append( [ int(fix(arq[i].split()[0],'a')), int(fix(arq[i].split()[2],'a')), float(arq[i].split()[4])])

		i+=1
	if flagfound == 1:
		ALLtrans.append(trans)
	i+=1


i = 0
for each in ALLtrans:
	print '\nSTATE:',selectedTrans[i],'--', selectedTransWL[i],'nm', '---------------'

	sumC = 0
	for j in range(len(ALLtrans[i])):
		sumC += ALLtrans[i][j][2]

	for trans in each:
		print '{:4s}'.format('H-'+str(abs(trans[0]-479))),trans[0],'->',\
			     trans[1],'{:4s}'.format('L+'+str(abs(trans[1]-480))),\
			 ' ','{:5.3f}'.format(trans[2]),'{:5.1f}'.format(100*trans[2]/sumC), '%'


	i+=1
