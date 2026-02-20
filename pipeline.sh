#!/bin/bash
echo "chunking data hitch3.txt"
cat hitch3.txt | python chonk.py
echo "Created partitions"
ls part* | xargs -n 1 -P 4 cat | python mapper.py | sort | python reducer.py > out
echo "Output generated in out"
#less out