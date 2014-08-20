#!/bin/bash
# Update the source code

[ `hostname` == seaman-sws ] && cat $pt/update.out && exit 0

doc-diff-all $jack src-jack


