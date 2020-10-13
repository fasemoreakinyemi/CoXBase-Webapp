#!/usr/bin/env sh
# -*- coding: None -*-
for files in $(ls ./*.fa)
do
        makeblastdb -in $files -parse_seqids -dbtype "nucl" 
done

