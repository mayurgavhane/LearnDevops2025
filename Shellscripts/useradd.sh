#!/bin/bash

#This script is for creation of new user

echo "==== Creation of new user started ===="

read -p "Enter user name" $username
read -p "Enter user password" $password

sudo useradd -m "$usesrname"
echo -e "$password\n$password" | sudo passwd"$username"

echo "==== User Creation is Completed ===="
