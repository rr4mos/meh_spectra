#!/bin/bash
cores=4
for file in $(find . -name \*.inp)
do
    echo $file
    name=`echo $file | cut -d'.' -f2` 

    # run in the background.
    /usr/lib64/mpi/gcc/openmpi/bin/orca $file > .$name.out &

    # Check how many background jobs there are, and if it
    # is equal to the number of cores, wait for anyone to
    # finish before continuing.
    background=( $(jobs -p) )
    if (( ${#background[@]} == cores )); then
        wait #-n
    fi
done
