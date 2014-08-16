#!/bin/bash
# Test the brain functionality

# List
echo brian list
rs brain list #| range 235 235

echo 'brian list(path=Git)'
rs brain list path=Git
rs brain list title='Plan' content='Market'

# Import
echo
echo brain import $HOME/Documents/MyBook/Public/ShrinkingWorld/Pricing
rs brain import $HOME/Documents/MyBook/Public/ShrinkingWorld/Pricing
echo
echo brain import $HOME/Documents/MyBook/Public/ShrinkingWorld
rs   brain import $HOME/Documents/MyBook/Public/ShrinkingWorld

#Show
echo
echo brain show  $HOME/Documents/MyBook/Public/ShrinkingWorld/Pricing
rs   brain show  $HOME/Documents/MyBook/Public/ShrinkingWorld/Pricing

# Errors
echo '-------------------------------------------'
echo 'Errors'
echo
echo brain import
rs brain import


echo
echo brain xxx
rs brain xxx

echo
echo brain
rs brain

echo
echo brain import xxx
rs brain import xxx
