#!/bin/bash

# check if file exists
if [ -f $1 ]
   then
        f=$(binwalk $1 | egrep -o '^[0-9]+')

        # extract files specified
        for i in $f; do
          if [ $i != 0 ]
             then
               dd if=./$1 of=./$i skip=$i bs=1
          fi
        done
fi
