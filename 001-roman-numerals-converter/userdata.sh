#!/bin/bash -x

# update the system
yum update -y

# install python and flash
yum install python3 -y
yum install pip -y
pip install flask

# install the code
cd /home/ec2-user

FOLDER="https://raw.githubusercontent.com/ikimukin/my-repository/refs/heads/main/001-roman-numerals-converter"
wget ${FOLDER}/app.py

mkdir templates
cd templates
wget ${FOLDER}/templates/index.html
wget ${FOLDER}/templates/result.html

cd ..

# run the app
python3 app.py
