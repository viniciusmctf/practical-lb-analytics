#!/bin/bash

RES_DIR="results"
TOP_DIR=$(pwd)
PLOT_FILE=$TOP_DIR/apptimes.dat
DATAFRAME=$TOP_DIR/apptimes.frame
rm $PLOT_FILE
touch $PLOT_FILE
echo Hello
cd $RES_DIR
for tasks in $(ls)
do cd $tasks
	for topos in $(ls)
  do cd $topos
		for freqs in $(ls)
    do cd $freqs
			BASE_FILE=${tasks}_${topos}_${freqs}
			for result in $(ls)
      do
        FILE=${result}_$BASE_FILE
        echo $FILE >> $PLOT_FILE
        cat $result | grep STEP.300 | awk\
        '{print $5}' >> $PLOT_FILE
      done
      cd ..
    done
    cd ..
  done
  cd ..
done

python3 $TOP_DIR/dicsvapptimes.py <<< $PLOT_FILE #> $DATAFRAME
mv apptimes.csv $TOP_DIR/
