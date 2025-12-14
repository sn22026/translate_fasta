# translate_fasta
## Translates FASTA files using translation table 2. 
This project was built to translate the longest ORF found in a FASTA file in order to prepare it for multiple sequence alignment. 

This project can:
1. Identify the longest ORF
2. Translate the longest ORF
3. Output the resulting amino acid sequence

Repository structure:
- assessment_biopython.py: biopython script to translate FASTA files
- folders A, B, C, D: contain reference sequences from BASH to be translated
- folder, c:/Users/lolaf/OneDrive/Desktop/Masters/Intro to bioinformatics/Assessment/A: contains the input and output files
- allfiles.fasta: the input file containing multiple FASTA files
- translated.fas: the output file containing translated ORFs

Installation and usage instructions:
1. [Install python](https://www.python.org/downloads/)
2. Install Biopython using "pip install biopython" in the python terminal.
