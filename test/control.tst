#!/bin/bash
# Control interface for data types


python $pb/util/control.py -list
python $pb/util/control.py -show

python $pb/util/control.py -add
python $pb/util/control.py -edit
python $pb/util/control.py -delete

python $pb/util/control.py -run
python $pb/util/control.py -test

python $pb/util/control.py -importfile
python $pb/util/control.py -exportfile


