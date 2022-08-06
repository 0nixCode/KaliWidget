#!/bin/bash
 
ip_address=$(cat $HOME/.config/bin/target/target.txt | awk '{print $1}')
machine_name=$(cat $HOME/.config/bin/target/target.txt | awk '{print $2}')
 
if [ $ip_address ] && [ $machine_name ]; then
    printf "<icon>w3af</icon>"
    printf "<txt> $ip_address - $machine_name</txt>"
    printf "<tool>Objetivo Localizado</tool>"
else
    printf "<icon>w3af</icon>"
    printf "<txt> Sin Objetivo</txt>"
    printf "<tool>Sin Objetivo</tool>"
fi
