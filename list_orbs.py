def fix(string,sgn):
	i = 0
	fixed=''
	while string[i] != sgn:
		fixed=fixed+string[i]
		i+=1
	return fixed

import sys

def getKey(item):
    return item[2]


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




extremes=file('TRANS_extreme.txt', 'w')

sortT = []
for i in range(len(ALLtrans)):
	sortT.append(sorted(ALLtrans[i], key=getKey, reverse=True))

for i in range(len(sortT)):
	ALLtrans[i]=sortT[i]

#i=0
#for each in ALLtrans:
#	print '***', selectedTrans[i]
#	for each2 in each:	
#		print  each2
#	print '***'
#	i+=1
#exit()
i = 0
for each in ALLtrans:
	print '\nSTATE:',selectedTrans[i],'--', selectedTransWL[i],'nm', '---------------'
	extremes.write('\nSTATE: '+str(selectedTrans[i])+' -- '+ str(selectedTransWL[i])+'  nm '+ '---------------\n')

	sumC = 0
	for j in range(len(ALLtrans[i])):
		sumC += ALLtrans[i][j][2]

## printing the transition list with all information

	for trans in ALLtrans[i]:
		print '{:4s}'.format('H-'+str(abs(trans[0]-479))),trans[0],'->',\
			     trans[1],'{:4s}'.format('L+'+str(abs(trans[1]-480))),\
			 ' ','{:5.3f}'.format(trans[2]),'{:5.1f}'.format(100*trans[2]/sumC), '%'

## printing the transition list with extremes informations only // UGLY 
	
	nbounds =len(ALLtrans[i])
#	print trans
#	exit()
	toprintTOP=[]
	toprintBOT=[]

	if nbounds > 4:
		for ii in range(2):
#			print ALLtrans[i]
#			print ALLtrans[i][ii][2],100*ALLtrans[i][ii][2]/sumC
			toprintTOP.append( 
                                     '{:4s}'.format('H-'+str(abs(ALLtrans[i][ii][0]-479))) +' '+\
				     str(ALLtrans[i][ii][0])+' -> '+\
				     str(ALLtrans[i][ii][1])+' {:4s}'.format('L+'+str(abs(ALLtrans[i][ii][1]-480)))\
                   		     +' '+str('  {:5.3f}'.format(ALLtrans[i][ii][2]))+\
                                     str('  {:5.1f}'.format(100*ALLtrans[i][ii][2]/sumC))+str( '%') )
#			print toprintTOP
						
			toprintBOT.append( 
                                     '{:4s}'.format('H-'+str(abs(ALLtrans[i][nbounds-ii-1][0]-479)))+' '+\
                                     str(ALLtrans[i][nbounds-ii-1][0])+' -> '+\
				     str(ALLtrans[i][nbounds-ii-1][1])+' {:4s}'.format('L+'+str(abs(ALLtrans[i][nbounds-ii-1][1]-480)))\
				     +' '+str('  {:5.3f}'.format(ALLtrans[i][nbounds-ii-1][2]))+\
                                     str('  {:5.1f}'.format(100*ALLtrans[i][nbounds-ii-1][2]/sumC))+str( '%') )
#				print toprintBOT
#				print toprintTOP
#				print 'here'
#				exit()

#		extremes.write('                             #strong\n')
		for any in toprintTOP:
			extremes.write(any+'    #strong  \n')

#		extremes.write('                             #weak\n')
		for any in toprintBOT:
			extremes.write(any+'    #weak\n')
					

	else:
		extremes.write("\n#see TRANS.txt\n\n")

	i+=1



