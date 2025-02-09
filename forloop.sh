#!/bin/bash

for NAMES in $(cat names.txt); do

    grep "M*"| echo "Names are: $NAMES"
done
