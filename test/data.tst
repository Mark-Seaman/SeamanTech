#!/bin/bash
# Test the data management commands

{

# Save an load entire data set
echo brain JSON file
json-save 
json-show brain | lc
json-load

# Save and load app data set
echo brain-doc JSON file
json-save-doc
json-show brain-doc | lc
json-load-doc

} | grep -v  'File:\|Installed'
