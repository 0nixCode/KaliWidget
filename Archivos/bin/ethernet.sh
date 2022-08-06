#!/bin/sh

ip="$(/usr/sbin/ifconfig eth0 | grep "inet " | awk '{print $2}')"

if [ "$ip" != "" ]; then
  printf "<icon>network-vpn-symbolic</icon>"
  printf "<txt> ${ip}</txt>"
  printf "<tool>Internet</tool>"
else
  printf "<icon>network-vpn-acquiring</icon>"
  printf "<txt> Sin Internet</txt>"
  printf "<tool>Sin Internet</tool>"
fi
