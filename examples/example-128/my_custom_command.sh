#!/bin/sh

if [ "$#" -eq "0" ]; then
   echo "[ERR 123] No files found.";
   exit 123;
fi

echo "Here I can do whatever I want wiht $@";
exit 0;
