#!/bin/bash
# Projects list

[ `hostname` == seaman-sws ] && cat $pt/projects.correct && exit 0

ls ~/Projects

