#!/bin/bash

rm ./step3_out.txt
rm ./step3_err.txt
touch ./step3_out.txt
touch ./step3_err.txt

times_run=0

while [[ $? -eq 0 ]];
do
    times_run=$((times_run+1))
    ./step3.sh 1>>./step3_out.txt 2>>./step3_err.txt
done

echo "The script ran $times_run times before resulting in an error"
