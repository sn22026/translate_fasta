#!/bin/bash

#Define output file
output="fastq_to_fasta"

#Remove old output
rm -f "$output"

#Loop all .fastq files
for file in *.fastq
do
#Make new files called {base}_clean.fasta
base="${file%.fastq}"
newfile="${base}_clean.fasta"
#Extract lines beginning with @, then lines beginning with + and the lines after it (i.e. the quality score)
sed '/^@/d; /^+/ {N;d}' "$file" > "$newfile"
echo "created: $newfile"
#Remove line breaks and replace spaces with Ns
tr -d '\n' <"$newfile" | tr ' ' 'N' > "${newfile}.tmp"
mv "${newfile}.tmp" "$newfile"
echo "removed line breaks in: $newfile"
done

