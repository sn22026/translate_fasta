# FASTQ to Translated ORF Pipeline
A bioinformatics pipeline for processing fragmented FASTQ sequencing data into translated amino acid sequences, ready for downstream multiple sequence alignment and phylogenetic analysis.
Built as part of an MSc Bioinformatics project. The pipeline converts and concatenates raw sequencing reads, identifies the longest open reading frame (ORF) in each assembly, and translates it to an amino acid sequence for use in phylogenetic workflows.

What this pipeline does

Converts FASTQ files to FASTA format
Concatenates fragmented FASTA files into a single file
Identifies the longest ORF in the concatenated sequence
Translates the ORF to an amino acid sequence
Outputs the resulting amino acid sequence for downstream analysis

Requirements

Git Bash
Python 3.x
Biopython (pip install biopython)

Usage
# Step 1: Convert and concatenate FASTQ files
bash fastq_to_fasta.sh
bash concatenate.sh

# Step 2: Translate the longest ORF
python assessment_biopython.py allfiles.fasta
Output will be written to translated.fas.

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
