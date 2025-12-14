# Import os
import os
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Data import CodonTable

# Change directory to folder containing FASTAs
os.chdir("c:/Users/lolaf/OneDrive/Desktop/Masters/Intro to bioinformatics/Assessment/A")

# Load FASTAs from one group
sequences = list(SeqIO.parse("allfiles.fasta", "fasta"))

# Store output amino acid objects
aa_sequences = []

# Choose translation table based on BLAST results
mito_table = CodonTable.unambiguous_dna_by_id[2]

# Get nucleotide sequence from FASTA
for record in sequences:
    dna_seq = record.seq
    # Store longest ORF across all frames
    longest_orf = ""
    # Store the frame containing longest ORF
    longest_frame = None
    # Translate sequence in all three forward reading frames
    for frame in range(3):
        # Translate starting at this frame and keep stop codons
        protein = dna_seq[frame:].translate(
            table=mito_table, to_stop=False)
# Split translation into orf fragments separated by stop codons ("*"),
        fragments = str(protein).split("*")

        # Find the longest ORF in this frame
        longest_in_frame = max(fragments, key=len)

        # If this ORF is longer than the best one so far, store it
        if len(longest_in_frame) > len(longest_orf):
            longest_orf = longest_in_frame
            longest_frame = frame

    # Convert the longest ORF string back into a Seq object
    longest_protein = Seq(longest_orf)

    # Extract Latin name from description line
    # Assumes format: >ID Genus species
    start = record.description.find("[organism=") + len("[organism=")
    end = record.description.find("]", start)
    latin_name = record.description[start:end].replace(
        " ", "_")  # replace space with underscore

    # Create a new SeqRecord containing the longest ORF for this sequence
    aa_record = SeqRecord(
        longest_protein,
        id=record.id,                      # Keep the same FASTA ID
        name=latin_name,                   # Store species name
        description=record.description,    # Preserve full original header
        annotations={
            "type": "longest ORF",
            "frame": longest_frame,  # Which reading frame the ORF came from
            "translation_table": mito_table
        }
    )

    aa_sequences.append(aa_record)         # Add to output list

# Write all translated longest-ORF sequences to a FASTA file
SeqIO.write(aa_sequences, "translated.fas", "fasta")
