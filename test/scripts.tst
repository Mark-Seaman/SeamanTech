#!/bin/bash
# Execute the system scripts

cd $pa && 

rs devtest     &&
rs  initialize &&

echo 'Scripts run successfully'
