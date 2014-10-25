#!/bin/bash
# Run nose to test python code

{

nosetests -v $p
nosetests -v $pb

} 2>&1 | sed 's/ in .*$//'
