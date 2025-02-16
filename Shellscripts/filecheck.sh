#!/bin/bash

while [ -f ~/test.txt ]; do 
    echo "$(date) The test file exist"
sleep 1
done
    
    echo "$(date) The file does not exist" 

