#!/bin/bash

for ((number = 0 ; number <= 10; number ++))
do
echo "The number is: $number"
done

for number in 1,3,5,7,9,11,13,15
do
  echo "This is random sequence number: $number"
done

for number in {1..8}
do
echo "This number is: $number"
done

number=1

while [ $number -le 10 ]
do
   echo $number
   number $(( $number+1 ))
done
 
 
