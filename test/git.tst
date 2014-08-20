#!/bin/bash
# Test the checked out files

cd $p
{
    echo $p 
    git status | grep -v 'nothing to commit'
} | filter-path
