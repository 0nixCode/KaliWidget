#!/bin/sh

ip="$(ip a s tun0 2>/dev/null | grep -o -P '(?<=inet )[0-9]{1,3}(\.[0-9]{1,3}){3}')"

if [ "$ip" != "" ]; then
  printf "<icon>draw-cuboid</icon>"
  printf "<txt> ${ip}</txt>"
  printf "<tool>VPN IP</tool>"
else
  printf "<icon>draw-cuboid</icon>"
  printf "<txt> Desconectado</txt>"
  printf "<tool>SIN VPN</tool>"
fi
