#!/bin/bash

# get permission
echo -e " Permissions : " >> ${1%%.*}_features.txt
awk '/E: uses-permission/ {f=NR} f && NR==f+1' $1  | sort -u >> ${1%%.*}_features.txt
echo -e "  " >> ${1%%.*}_features.txt

# get intents action
echo -e " Intents Action : " >> ${1%%.*}_features.txt
awk '/E: action/ {f=NR} f && NR==f+1' $1 | sort -u >> ${1%%.*}_features.txt
echo -e "  " >> ${1%%.*}_features.txt

# get service
echo -e " Services : " >> ${1%%.*}_features.txt
awk '/E: service/ {f=NR} f && NR==f+1' $1 | sort -u >> ${1%%.*}_features.txt
echo -e "  " >> ${1%%.*}_features.txt

# get intent category
echo -e " Intents Category : " >> ${1%%.*}_features.txt
awk '/E: category/ {f=NR} f && NR==f+1' $1 | sort -u >> ${1%%.*}_features.txt
echo -e "  " >> ${1%%.*}_features.txt

