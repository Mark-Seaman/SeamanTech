#!/bin/bash
# Watch for changes in the docs

cd $pd
find | sort | grep -v '\.out' | range 3000 3500 
