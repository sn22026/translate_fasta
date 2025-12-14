# translate_fasta
## Converts fragmented FASTQ files into concatenated FASTA files, then translates them. 
This project was built to assimilate fragmented FASTQ samples into FASTA files in Git Bash, then the output was moved to python to translate the longest ORF found in a FASTA file in order to prepare it for multiple sequence alignment. 

This project can:

1. Convert FASTQ files to FASTA files
2. Concatenate fragmented FASTA files
3. Identify the longest ORF
4. Translate the longest ORF
5. Output the resulting amino acid sequence

Repository structure:
- fastq_to_fasta.sh: shell converting FASTQ files to FASTA files
- concatenate.sh: shell concatenating the outputs from fastq_to_fasta.sh
- samples: the fragmented FASTQ files 
- assessment_biopython.py: biopython script to translate FASTA files
- folders A, B, C, D: contain reference sequences from BASH to be translated
- folder, c:/Users/lolaf/OneDrive/Desktop/Masters/Intro to bioinformatics/Assessment/A: contains the input and output files
- allfiles.fasta: the input file containing multiple FASTA files
- translated.fas: the output file containing translated ORFs

Installation and usage instructions:
1. [Install Git Bash](https://gitforwindows.org/)
2.  [Install python](https://www.python.org/downloads/)
3. Install Biopython using "pip install biopython" in the python terminal.
