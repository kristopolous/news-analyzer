#!/bin/sh

while [ 0 ]; do
  ./pull.py
  for i in `seq 90 -1 1`; do
    echo -n "$i "
    sleep 10
  done
done

