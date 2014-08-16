#!/bin/bash
# Read and write tables

# Run nose to test python code
cd $pb
nosetests 2>/dev/null

# Show the requested file output
function show
{
    echo
    echo $1
    lc $1
    cat $1
    echo
}

show /tmp/data.csv
