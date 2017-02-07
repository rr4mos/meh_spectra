def cleaN(string):
	cstr =''
	i=0 
	while string[i]!='.':
		cstr=cstr+string[i]
		i+=1
	return cstr

import sys

# RR 2016


Emax = 600       # topo da janela
Emin = 400       # topo da janela
N   = 200        # int(sys.argv[1])
sig = 10         # lorentzian broadening parameter
E0 = Emin - 00.0 # 
Ef = Emax + 00.0 # 

dE = (Ef - E0)/N

print '\nSoma de espectros com Broadening Lorentziano'
print '---------------------------------------------'
print 'janela:', Emax, '--', Emin, 'nm'
print 'N:',N,'dE', dE
print 'sig:', sig, 'nm'
print '---------------------------------------------\n\n'

name=sys.argv[1]
arq = file(name,'r').readlines()

cname = cleaN(name)
print cname

En = []
Os = []
for line in arq:
	if len(line.split()) > 1:
		En.append(float(line.split()[0]))
		Os.append(float(line.split()[1]))


Spec = []
E = []
for i in range(N+1):
	Spec.append(0.0)
	E.append(E0+i*dE)



#Lorentziana: Os -> L(E) = Os(En)/( ((E-En)/sig)**2 + 1)
#full spec: sum_chain Os_chain

for i in range(len(Os)):
	if En[i] > Emin and En[i] < Emax:
		for e in range(len(E)):
			L = Os[i]/( ((E[e]-En[i])/sig)**2 + 1)
			Spec[e]= Spec[e]+L
			#print 'lrtz:', E[e],L

# AVOIDING NORMALIZATIONS

maxSpec = 1.0 #max(Spec)
minSpec = 0.0 #min(Spec)
Norm    = 1.0 #maxSpec - minSpec
arqout = file(cname+'-UV_WITHOUTNORM_'+str(sig)+'nm'+'.dat','w')
for e in range(len(E)):
	arqout.write('{:6.1f}'.format(E[e])+' '+\
		     '{:6.4f}'.format((Spec[e]-minSpec)/Norm)+'\n')


arqout.close()

# delta specs normalizados
arqout = file(cname+'full-deltaSpecNorm.dat','w')
for i in range(len(Os)):
	if En[i] > Emin and En[i] < Emax:
		arqout.write( '{:6.1f}'.format(En[i])+' '+\
	      		      '{:6.4f}'.format(Os[i]/Norm)+'\n')
		
arqout.close()




