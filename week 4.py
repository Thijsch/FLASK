# Thijs Ermens
# 11 mei 2020
# DNA-sequenties omzetten naar eiwit

from bio.Alphabet import IUPAC
from bio.Seq import Seq
from bio.Data import CodonTable
from bio import SeqIO


def seq_bewerken(seq, mito_trans_table, standard_trans_table):
    """
    Sequentie naar biopython object omzetten
    sequentie transleren naar eiwit
    :param seq: DNA-sequentie die omgezet moet worden naar eiwit
    :return:
    """

    bio_dna = Seq(seq, IUPAC.unambiguous_dna)
    print(bio_dna.translate(table=standard_trans_table))

    def conversie_gb_to_fasta(genbank_file, name_fasta_file):
        """

        :param genbank_file:
        :param name_fasta_file:
        :return:
        """
        with open(genbank_file, "r") as inFile:
            with open(name_fasta_file, "w") as output:
                sequences = SeqIO.parse(inFile, "genbank")
                fasta = SeqIO.write(sequences, output, "fasta")

    def parse_fasta(fasta_file):
        """
        Fasta bestand parsen
        :param fasta_file: str - naam van fasta bestand
        :return:
        """
        with open(fasta_file) as inFile:
            for seq_record in SeqIO.parse(inFile, "fasta"):
                print(seq_record.id)
                print(seq_record.seq)

if __name__ == '__main__':
    seq = 'ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG'
    mito_trans_table = CodonTable.unamibuous_dna_by_name["Vertebrate Mitochondrial"]
    standard_trans_table = CodonTable.unamibuous_dna_by_name["Standard"]

    seq_bewerken(seq, mito_trans_table, standard_trans_table)