#!/bin/bash

# Just replace the package in venv
PROJECT=shmalexa
DIR=$(find venv/ -type d -name $PROJECT | tr -d '\n')
rm -rf $DIR
cp -r $PROJECT $DIR
