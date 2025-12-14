#!/bin/bash

#loop the fastas
for group in A B C D
do
output="${group}_concat.fasta"

#concatenate files from same group
cat ${group}*_clean.fasta >> "$output"

#add header to concatenated fastas
sed -i "1i>Unknown_sample_${group}" "$output"

echo "Created: $output"
done

