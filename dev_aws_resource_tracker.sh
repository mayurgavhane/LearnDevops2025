#!/bin/bash

#################
#Author: Mayur
#Date: 31st Jan 2025
#Version: V1

#################
set -x

#This script will list mentioned AWS resources

#AWS Lambda

#list lambdas
echo "List of lambdas"
aws lambda list-functions | grep "Template"

