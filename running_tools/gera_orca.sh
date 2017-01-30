## executar no diretorio com os pdbs 
## colocar nesse diretorio o arquivo head.inp

for file in $(find . -name \*pdb)
do
	echo "pdb file: $file"
	name=`echo $file | cut -d'.' -f2` 

	babel $file -oxyz .$name.xyz

# gerando o input
	nat=`cat .$name.xyz | wc -l `
	nat=$(($nat-2))
	echo "number of atoms: " $nat
	cat head.inp > .$name.inp
	echo "* xyz 0   1" >>.$name.inp
	tail -n $nat .$name.xyz >> .$name.inp
	echo "*" >> .$name.inp

	echo "orca input file: .$name.inp"
done
