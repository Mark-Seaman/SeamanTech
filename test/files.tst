#!/bin/bash
# File list test

{
    ls $p $p/* | grep -v 'pyc$\|diff$\|out$\|like$'
} | filter-path
