#!/bin/bash
# Execute the system scripts

cd $pa && 

rs devtest     &&
rs  initialize &&

#rs test_doc
#rs test_time

echo 'Scripts run successfully'
