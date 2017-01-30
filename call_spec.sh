pack='/home/rramos/Dropbox/MEHPPV-ComputMat2016/work/results/optica/pack_anl_spec/'

home=`pwd`
ntrans=30
for dir in $(find . -name \[A-Z] | sort)
do
	echo $dir
	cd $dir
	file=`ls -1 *.out`
	echo $file
	python $pack/getTrans.py $file $ntrans > TransLabels.in
	python $pack//list_orbs.py $file > TRANS.txt
	namespec="$file"_"$ntrans"_trans.txt
	python $pack/sum_spec_broadening.py $namespec
	nameoutspec=`echo "$file" | cut -d'.' -f1`

#	gnuplot check // begin
	echo $nameoutspec
	nameoutspec="$nameoutspec""full-UV_Lbroad-10nm.dat"
	echo $nameoutspec
	echo "" > .pltspec
	echo "set terminal png" >> .pltspec
	echo "set output 'spec.png'" >> .pltspec

	echo "plot [400:600][0:1]'$nameoutspec' w l,\\" >> .pltspec
	nameoutspec=`echo "$file" | cut -d'.' -f1`
	echo $nameoutspec
	nameoutspec="$nameoutspec""full-deltaSpecNorm.dat"
	echo "'$nameoutspec' with impulses" >> .pltspec
#	echo "pause -1" >> .pltspec
	gnuplot .pltspec	
#	gnuplot check //end 


#	exit
#	gnuplot ../pack_anl_spec/plota_gnuplot.gnu
	cd $home
done 

