#!/bin/bash

RES_DIR="results"
TOP_DIR=$(pwd)
PLOT_FILE=$TOP_DIR/plots.dat
rm $PLOT_FILE
touch $PLOT_FILE
echo Hello
cd $RES_DIR
for tasks in $(ls)
do
	cd $tasks
	for topos in $(ls)
  do
		cd $topos
		for freqs in $(ls)
    do
			cd $freqs
			BASE_FILE=${tasks}_${topos}_${freqs}
			for result in $(ls)
      do
        echo "${BASE_FILE}_$result"
        echo "${BASE_FILE}_$result" >> $PLOT_FILE
				cat $result | egrep STEP | awk '{print $4, $6}' | python3 $TOP_DIR/calc_histo_mean.py >> $PLOT_FILE
			done
			cd ..
		done
		cd ..
	done
	cd ..
done
