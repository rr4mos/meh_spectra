
for file in $(ls -1 *.out)
do
	echo $file
	NAME=`echo "$file" | cut -d'.' -f1`
	NAME=`echo "$NAME" | cut -d'_' -f2`

	echo $NAME
	mkdir $NAME 
	mv $file $NAME

done
