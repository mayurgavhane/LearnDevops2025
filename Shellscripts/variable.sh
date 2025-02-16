#!/bin/bash



name=$1
compliment=$2i
user=$(whoami)
date=$(date)
directory=$(pwd)

echo "Hello $name"
sleep 1
echo "How are you today $name"
sleep 1
echo "This is your $compliment  day $name"
sleep 1
echo "You are logged in as $user"
echo "Todat is $date"
echo "You are in this directory: $directory"

