#!/bin/bash
# Projects list

h=`hostname`
[ "$h" != "seaman-hammer" ] && 
tcorrect $pt/projects && 
exit 0

ls ~/Projects

