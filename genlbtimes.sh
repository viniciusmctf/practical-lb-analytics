#!/bin/bash

RES_DIR="results"
TOP_DIR=$(pwd)
PLOT_FILE=$TOP_DIR/lbtimes.dat
DATAFRAME=$TOP_DIR/lbtimes.frame
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
        cat $result | grep "step .* finished at .* duration" | awk\
        '{if ($1 == "CharmLB>") print $6, $11; else if ($1 == "[HybridLB]") print $5,$10; else print $3, $8}'>> $PLOT_FILE
      done
      cd ..
    done
    cd ..
  done
  cd ..
done

python3 $TOP_DIR/dicsvlbtimes.py <<< $PLOT_FILE #> $DATAFRAME
mv lbtimes.csv $TOP_DIR/
