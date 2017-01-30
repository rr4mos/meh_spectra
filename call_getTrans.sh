for file in $(find . -name \*.out)
do
	echo $file
	python ../pack_anl_spec/getTrans.py $file 30 
done


