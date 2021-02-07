#!/usr/bin/env bash

create(){
    echo "BOT_TOKEN = " >> ../.env
    if ! command -v virtualenv &> /dev/null
    then
        echo -e "\n'virtualenv' could not be found, installing:\n----------"
        pip3 install virtualenv   
    fi
    echo "----------"
    virtualenv ../venv
}

create

echo -e "\n----------\nCompleted! Now just activate the environment.\n"