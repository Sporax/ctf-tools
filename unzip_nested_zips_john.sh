#!/bin/bash

# 419 times
for i in {418..2}
do
./tools/john/run/zip2john level${i}.zip > shadow
./tools/john/run/john shadow --wordlist=tools/other/rockyou.txt
unzip -P $(cat tools/john/run/john.pot | rev | cut -f1 -d':' | rev | tail -n 1) level${i}.zip
done
