#!/bin/bash
#
#This scrip will automate user creation, modification and deletion
#

function user_creation
{
echo "User creation had started"

read -p "Enter user name: " username
sudo useradd -m $username

echo "User is now created"
}
for ((i=1;i<=5;i++))
do 
	user_creation
done

function user_modification
{
echo "Enter the user name which should be updated" 
read -p "Enter user name: " username
sudo usermod -aG $username  Madhu

echo "User has been added to new group"
}
for ((i=1;i<=5;i++))
do user_modification
done

function user_deletion
{
echo "Enter the user name which should be deleted"
read -p "Enter the user name: " username
sudo userdel $username

echo "User has been deleted now"
for ((i=1;i<=5;i++))
do 
	user_deletion
done

}
